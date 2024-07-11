from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Post, Conta, Like, Save
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm, UserRename

def home(request):
        profile_button =request.POST.get('profile_button')
        posts = Post.objects.all().order_by('-id')
        user= request.user
        conta = get_object_or_404(Conta, user=user)
        profile_path = request.POST.get('profile_path')
        new_post = request.POST.get('new_post')
        if new_post:
            image = request.FILES.get('image_button')
            post_text = request.POST.get('new_post_text')
            if post_text:
                New_post =  Post.objects.create(author_profile=conta, image=image, text=post_text)
                New_post.save()
            else:
                return render(request, 'pages/home.html', context={
            'posts': posts,
            'conta': conta,
            'is_home': True,
            'error' : True
            })
                
        if not profile_button:
            return render(request, 'pages/home.html', context={
            'posts': posts,
            'conta': conta,
            'is_home': True
            })
        else: 
            return profile_page(request, conta.id)
 
    
def login_page(request):
    if request.method== 'GET':
        Conta.objects.all().delete()
        Post.objects.all().delete()
        Like.objects.all().delete()
        Save.objects.all().delete()
        return render(request, 'pages/login_page.html', context={
        })
    else:
        email= request.POST.get('email')
        password = request.POST.get('password')
   
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user, backend='Vitornet_app.backends.EmailBackend')
            return redirect('home/')
        else: 
             return render(request, 'pages/login_page.html', context={
        'error': True})
    
 
def create_cont(request):
    if request.method == 'GET':
        return render(request, 'pages/login_page.html', context={
            'create_cont' : True,
        })
    else:
        
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']    
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
             
            user = User.objects.create_user( username=username, email=email, password=password,last_name=last_name, first_name=first_name)
            user.save()

        
            conta = Conta.objects.create(user=user)
            login(request, user, backend='Vitornet_app.backends.EmailBackend')
            return home(request)
        else:
           return render(request, 'pages/login_page.html', context={
                    'create_cont' : True,
                    'form': form
                })
def profile_page(request, cont_id):
    conta= get_object_or_404(Conta, id=cont_id)
    posts = Post.objects.filter(author_profile__user=request.user).order_by('-id')
    saves = Save.objects.filter(user=request.user).order_by('-id')
    saved_posts = [save.post for save in saves]
    likes = Like.objects.filter(user=request.user).order_by('-id')
    liked_posts = [like.post for like in likes]
    return render(request, 'pages/profile_page.html', context={
        'conta': conta,
        'posts': posts,
        'saves': saved_posts,
        'likes': liked_posts,
        'is_profile_page': True
    }) 
def like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    liked = Like.objects.filter(user=request.user, post=post).first()

    if liked:
        liked.delete()
        post.likes -= 1
        liked_status = False
    else:
        Like.objects.create(user=request.user, post=post)
        post.likes += 1
        liked_status = True 

    post.save()  

    return JsonResponse({
        'likes': post.likes,
        'liked': liked_status
    })

def save(request, post_id):
      post = get_object_or_404(Post, id=post_id)
      saved = Save.objects.filter(user=request.user, post=post).first()
    

      if saved:
          saved.delete()  
          saved_status = False
      else:
          Save.objects.create(user=request.user, post=post)
          saved_status = True

      return JsonResponse({
          'saved': saved_status
      })


def ChangeName(request):
    user = request.user
    conta = get_object_or_404(Conta, user=user)
    id = conta.id
    newname = request.POST.get('username')
    form = UserRename(request.POST)
    if form.is_valid():
        user.username = newname
        user.save()
        return profile_page(request, id)
    else:
     return profile_page(request, id)
    
def ChangePicture(request):
        user = request.user
        conta = get_object_or_404(Conta, user=user)
        conta.picture = request.FILES.get('login_page_profile_picture_hover')
        conta.save()

        return profile_page(request, conta.id)