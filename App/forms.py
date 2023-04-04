from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, label="Imię") 
    last_name = forms.CharField(max_length=50, label="Nazwisko")
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name', 'password1', 'password2',]
        
class CreatePost(ModelForm):
    class Meta:
        model = Post
        labels = {
            'text': 'Opis',
            'image': 'Obraz',
        }
        widgets = {
          'text': forms.Textarea(attrs={'rows':3,}),
        }
        fields = ['text', 'image']
        
class EditProfile(ModelForm):
    class Meta:
        model = UserProfile
        widgets = {
          'profile_description': forms.Textarea(attrs={'rows':1,}),
        }
        labels = {
            'name': 'Imię',
            'last_name': 'Nazwisko',
            'profile_description': 'Opis profilu',
            'profile_pic': 'Zdjęcie profilowe',
        }
        
        exclude  = ['user','email','followers']
        
        