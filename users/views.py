from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

from main.utils import list_friends
from .forms import AuthenticationForm, RegisterProfileFrorm, RegisterUserForm, CustomePasswordResetForm
from .models import Profile, Friend
from django.contrib.auth import authenticate, login, logout
from .utils import user_without_username 
from django.contrib.auth.views import PasswordResetView  
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from post.forms import PostForm
import json
from post.models import Post
# Create your views here.




def in_account(request): 
    if request.method == 'POST': 
        form = AuthenticationForm(data=request.POST) 
        if form.is_valid():  
            cd = form.cleaned_data 
            username = user_without_username(cd)
            user = authenticate(request, username=username, password=cd['password']) 
            if user is not None: 
                login(request, user)
                return redirect('main:index')
            else: 
                return HttpResponse('not user')

    else: 
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'users/auth/auth.html', context=context)  

@login_required
def from_log(request):  
    logout(request) 
    return redirect('users:login')



def register(request): 
    if request.method == "POST": 
        form_user = RegisterUserForm(request.POST) 
        form_profile = RegisterProfileFrorm(request.POST) 

        if form_user.is_valid() and form_profile.is_valid(): 
            user = form_user.save(commit=False) 
            user.set_password(form_user.cleaned_data['password'])  
            user.save()  

            profile = form_profile.save(commit=False) 
            profile.user = user
            profile.save() 

            return redirect('users:login')  
    else:
        form_user = RegisterUserForm() 
        form_profile = RegisterProfileFrorm() 


    context = {
        'form_user': form_user, 
        'form_profile': form_profile,
    }
    return render(request, 'users/auth/register.html', context=context) 




class CustomeResetPasswordView(PasswordResetView): 
    template_name = 'users/auth/reset_password/reset_password.html' 
    success_url =  reverse_lazy('users:password_reset_done')  # поки тест потім зміні  
    #from_email = 'macmo20010218@gmail.com'    
    email_template_name = 'users/auth/reset_password/email_reset_password.html'
    form_class = CustomePasswordResetForm


@login_required
def add_friend(request, user_id):
    user_to_friend = get_object_or_404(User, id=user_id) 
    Friend.objects.create(from_user=request.user, to_user=user_to_friend)
    messages.success(request, f"You are friend")
    return redirect(request.META.get('HTTP_REFERER', '/'))



@login_required
def remove_friend(request, user_id):
    user_to_remove = get_object_or_404(User, id=user_id)
    Friend.objects.filter(
        Q(to_user=request.user, from_user=user_to_remove)|
        Q(to_user=user_to_remove, from_user=request.user)
    ).delete()
    messages.success(request, f"You removed  {user_to_remove.first_name}.")
    return redirect(request.META.get('HTTP_REFERER', '/')) 


@login_required(login_url='users:login')
def friends(request): 
    friends  = list_friends(request.user) 
     
    context = {'friends': friends}
    return render(request, 'users/friends.html', context=context) 


@login_required(login_url='users:login')
def profile_user(request, username):  
    user = get_object_or_404(User, username=username) 
    profile = get_object_or_404(Profile, user=user) 
    friends  = list_friends(request.user)[:3] 

    draft_post, created = Post.published.get_or_create(owner=request.user) 

    if request.method == 'POST':  
        if request.content_type == 'application/json': 

            new_s = json.loads(request.body)   
            draft_post.text += new_s['text']
            draft_post.save()  
        else: 
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():  
                draft_post.save_pb()
                return redirect(request.META.get('HTTP_REFERER', '/')) 

    form = PostForm() 
    context = {'profile': profile, 'user': user, 'friends': friends, 'form': form, 'draft_post': draft_post.text}
    return render(request, 'users/user_profile.html', context=context)