from django.shortcuts import get_list_or_404, redirect, render
from .models import Post, Comment 
from .forms import PostForm, CommentForm
# Create your views here.
from django.contrib.auth.decorators import login_required 
from django.views.decorators.http import require_GET, require_POST


@login_required(login_url='users:login')
def create_post(request):  
    #post = Post.objects.create(user=request.user, status=Post.STATUS_CHOICES.Draft) 
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid(): 
            post = form.save(commit=False) 
            post.user = request.user 
            post.save() 
            return redirect('post:list_post', request.user.id)
    else: 
        form = PostForm()


    context = {'form': form, 'test': 'test_something'}
    return render(request, 'post/create_post.html', context=context) 


@login_required(login_url='users:login')
def list_post(request, user): 
    list_posts = get_list_or_404(Post, user=user) 

    return render(request, 'post/list_post.html', {'list_posts': list_posts})



