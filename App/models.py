from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    profile_pic = models.ImageField(null=True, blank=True, default='user.png')
    followers = models.ManyToManyField('self',blank=True, symmetrical=False)
    profile_description = models.CharField(max_length=150, null=True)

    def __str__(self):
        return f"{self.name} {self.last_name}"
    
class Post(models.Model):
    userprofile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='posts')
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(null=True)
    viewCount = models.IntegerField(default=0)
    likes = models.ManyToManyField(UserProfile, blank=True)
    
    class Meta:
        ordering = ('-creation_date',)
    def __str__(self):      
        if self.text[50:]:
            return f"Post created by:{self.userprofile}, text: {self.text[:50]}..."
        else:
            return f"Post created by:{self.userprofile}, text: {self.text[:50]}"
    
    
    
    
class PostComment(models.Model):
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='user_post_comment',)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_comment",)
    text = models.CharField(max_length=100, null=True, blank=True,)
    creation_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} commented {self.post}"

    


