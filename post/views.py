from django.shortcuts import get_list_or_404, redirect, render
from .models import Post, Comment 
from .forms import PostForm, CommentForm
# Create your views here.
from django.contrib.auth.decorators import login_required 
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.models import User 
import json

# @login_required(login_url='users:login')
# def create_post(request):  
#     #post = Post.objects.create(user=request.user, status=Post.STATUS_CHOICES.Draft) 
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid(): 
#             post = form.save(commit=False) 
#             post.user = request.user 
#             post.save() 
#             return redirect('post:list_posts', request.user.username)
#     else: 
#         form = PostForm()


#     context = {'form': form, 'test': 'test_something'}
#     return render(request, 'post/create_post.html', context=context) 
# @login_required(login_url='users:login')
# def create_post(request):  
#     if request.method == 'POST':
#         # scope 1 - form
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid(): 
#             post = form.save(commit=False) 
#             post.user = request.user 
#             post.save() 
#             return redirect('user:profile')
#         # if form is not valid - this context renders form from scope1
#         context = {'form': form}
#         return render(request, 'post/create_post.html', context=context)
#     # this will cach if request.method is not POST
#     # scope 2 - form
#     form = PostForm()
#     # scope 2 - context (same scope as form)
#     context = {'form': form}
#     return render(request, 'post/create_post.html', context=context)

@login_required()
def list_post(request, username):  
    owner = User.objects.get(username=username)
    list_posts = get_list_or_404(Post, owner=owner, status='Pb')[::-1]  
    

    context = {'list_posts': list_posts}

    return render(request, 'post/list_post.html', context=context)



def post(request, post_id): 
    post = Post.objects.get(id=post_id)  
    users_comment = post.comment_post.filter(owner=request.user).order_by()
 


    if request.method == 'POST': 
        action = json.loads(request.body)['action']  

        # перевірити
        if action == 'like':  
            if request.user in  post.like.all():  
                post.like.remove(request.user)
            else:
                post.like.add(request.user) 
        else: 
            if request.user in  post.dislike.all():  
                post.dislike.remove(request.user)
            else:
                post.dislike.add(request.user)

    context = {'post': post}

    return render(request, 'includes/post_comment.html', context=context)