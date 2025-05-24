from django.shortcuts import get_list_or_404, redirect, render
from .models import Post, Comment 
from .forms import PostForm, CommentForm
# Create your views here.
from django.contrib.auth.decorators import login_required 
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.models import User 
import json
from django.db.models import Count 
from itertools import chain

@login_required()
def list_post(request, username):  
    owner = User.objects.get(username=username)
    list_posts = get_list_or_404(Post, owner=owner, status='Pb')[::-1]  
    

    context = {'list_posts': list_posts}

    return render(request, 'post/list_post.html', context=context)



def post(request, post_id): 
    post = Post.objects.get(id=post_id)  
    #comment = Comment.objects.get(post=post, id=comment_id) 
    
    


    
    if request.method == 'POST' : 
        data = json.loads(request.body) 


        if data['action']:  
            action = data['action'] 
            query_action = getattr(post, action)
            query_action.remove(request.user) if request.user in  query_action.all() else   query_action.add(request.user)
        # try:
        #     action = data['action']  

        #     # перевірити
        #     if action == 'like':  
        #         post.like.remove(request.user) if request.user in  post.like.all() else   post.like.add(request.user)
        #     else: 
        #         post.dislike.remove(request.user) if request.user in  post.dislike.all() else post.dislike.add(request.user) 
        # except:  
        else:
            
            text_comment = data['text_comment']
            Comment.objects.create(
                owner=request.user, 
                text=text_comment, 
                post=post,
            )
     



    

    return render(request, 'post/list_post.html')