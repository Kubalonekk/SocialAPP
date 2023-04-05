from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from datetime import datetime
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import *
from django.contrib.auth.decorators import user_passes_test

def login_check(user):
    return user.is_authenticated



@user_passes_test(login_check, login_url='/check/')
def index(request):
    profile = UserProfile.objects.get(user=request.user)   
    posts = Post.objects.filter(Q(userprofile__in=profile.followers.all())).order_by('-creation_date')
    paginator = Paginator(posts, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == "POST":
        post_comment  = request.POST.get('post_comment')
        id = request.POST.get('id')
        new_post_comment = PostComment.objects.create(
            user=request.user.userprofile,
            post_id=id,
            text=post_comment,
        )
        messages.success(request, 'Dodałeś nowy komentarz')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))    

    context = {
        'posts' : posts,
        'page_obj': page_obj,
        
    }

    return render(request, 'App/index.html', context)

@user_passes_test(login_check, login_url='/check/')
def add_or_remove_follow(request, pk):
    user = request.user.userprofile
    profile = UserProfile.objects.get(pk=pk)
    if profile in user.followers.all():
        user.followers.remove(profile)
        messages.success(request, 'Przestałeś obserwować użytkownika ' + profile.name +' '+ profile.last_name )
    else:
        user.followers.add(profile)
        messages.success(request, 'Zacząłeś obserwować użytkownika ' + profile.name +' '+ profile.last_name )
    
    return redirect('user_profile', pk)

@user_passes_test(login_check, login_url='/check/')
def add_or_remove_like(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user.userprofile
    if user in post.likes.all():
        post.likes.remove(user)
        messages.success(request, 'Przestałeś lubić post')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    else:
        post.likes.add(user)
        messages.success(request, 'Polubiłeś post')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))    
    
@user_passes_test(login_check, login_url='/check/')
def post(request, pk):
    post = Post.objects.get(pk=pk)
    
    context = {
        'post': post,
    }
    
    return render(request, 'App/post.html', context)

@user_passes_test(login_check, login_url='/check/')
def your_profile(request):
    user = UserProfile.objects.get(user=request.user)
    posts = user.posts.all()
    post_counter = posts.count()
    followers = UserProfile.objects.filter(followers=user).count()
    following = user.followers.count()
 
    context ={
        'user': user,
        'posts': posts,
        'followers': followers,
        'following': following,
        'post_counter': post_counter,     
        
    }
    
    return render(request, 'App/your_profile.html', context)



@user_passes_test(login_check, login_url='/check/')
def user_profile(request, pk):
    user = UserProfile.objects.get(pk=pk)
    if user == request.user.userprofile:
        return redirect('your_profile')
    else:
        pass
    posts = user.posts.all()
    post_counter = posts.count()
    followers = UserProfile.objects.filter(followers=user).count()
    following = user.followers.count()

    
    context ={
        'user': user,
        'posts': posts,
        'followers': followers,
        'following': following,
        'post_counter': post_counter,     
        
    }
    
    return render(request, 'App/user_profile.html', context)


@user_passes_test(login_check, login_url='/check/')
def add_post(request):
    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.userprofile = request.user.userprofile
            new_post.save()
            messages.success(request, 'Pomyślnie dodano post')
            return redirect('index')             
    else:
        form = CreatePost()
        
    context = {
        'form': form,
    }
    return render(request, 'App/add_post.html', context)


def login_check(user):
    return user.is_authenticated


@user_passes_test(login_check, login_url='/check/')
def friends(request):
    if request.method == "POST":
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        search_user = UserProfile.objects.filter(
            Q(name__icontains=name) & Q(last_name__icontains=last_name)).order_by('-creation_date')
        title = "Twoje wyszukanie"
    else:
        title = "Nowi użytkownicy"
        search_user = UserProfile.objects.all().order_by('-creation_date')[:3]
        
    context = {
        'search_user': search_user,
        'title': title,
    }
    
    return render(request, 'App/friends.html', context)





@user_passes_test(login_check, login_url='/check/')
def edit_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        form = EditProfile(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pomyśnie edytowano profil' )
    else:
        form = EditProfile(instance=profile)
    
    context = {
        'profile': profile,
        'form': form,
    }
    
    return render(request, 'App/edit_profile.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            NewUserProfile = UserProfile.objects.create(
                user=new_user,
                name=first_name,
                last_name=last_name,
                email=email,
            )
            NewUserProfile.followers.add(NewUserProfile)
            authenticated_user = authenticate(
                username=new_user.username,
                password=request.POST['password1'])
            login(request, authenticated_user)
            messages.success(request, 'Pomyślnie założno konto')
            return redirect('index')
    else:
          form = UserRegisterForm()
          
    context = {
        'form': form,
    }
    return render(request, 'App/register.html', context)
        
@user_passes_test(login_check, login_url='/check/')
def signout(request):
    logout(request)
    messages.success(request, 'Pomyślnie wylogowano')
    return redirect('login/')

      
        
def check(request):
    if request.user.is_anonymous:
        messages.warning(request, 'Musisz być zalogowany żeby mieć dostęp do tej strony')
        return redirect('/login/')
    


def custom_page_not_found_view(request, exception):
    return render(request, "App/404.html", {})


