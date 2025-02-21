from django.shortcuts import render
from .models import Post, Comment 
from .forms import PostForm, CommentForm
# Create your views here.
from django.contrib.auth.decorators import login_required 


@login_required(login_url='users:login')
def create_post(request): 
    if request.method == 'POST': 
        form = PostForm(request.POST, request.FILES) 
        if form.is_valid():
            new_post = form.save(commit=False)  
            new_post.user = request.user 
            new_post = form.save() 
            return render(request, 'post/create_post.html')
    else: 
        form = PostForm() 
    context = {'form': form}
    return render(request, 'users/user_profile', context=context)



