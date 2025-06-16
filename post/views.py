from django.shortcuts import get_list_or_404, redirect, render
from django.urls import reverse
from .models import Post, Comment 
from .forms import PostForm, CommentForm
# Create your views here.
from django.contrib.auth.decorators import login_required 
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.models import User 
import json
from django.db.models import Count 
from itertools import chain
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django.views.decorators.cache import cache_page

from rest_framework.views import APIView
from .serializers import CommentSerialezers
from rest_framework.response import Response

@login_required()
def list_post(request, username):  



    owner = User.objects.get(username=username)
    #list_posts = get_list_or_404(Post, owner=owner, status='Pb')[::-1]  
    list_posts = Post.objects.filter(owner=owner, status='Pb').order_by('-create_time')   


    paginator = Paginator(list_posts, 2)
    page_number = request.GET.get("page", 1)  

    if  int(page_number) > paginator.num_pages: 
        return redirect(request.path)

    page_obj = paginator.get_page(page_number) 

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':  
        
        add_content = render_to_string('includes/post_list.html', context={'list_posts': page_obj}, request=request)  
        return JsonResponse({"new_page": add_content})  



    

    context = {'list_posts': page_obj, "next_page": page_obj.has_next()}

    return render(request, 'post/list_post.html', context=context)



def post(request, post_id): 
    post = Post.objects.get(id=post_id)  
    
    if request.method == 'POST' : 
        data = json.loads(request.body) 

        action = data['action'] 

        if data['action'] in ['like', 'dislike']: 
             
            model = data['type'] 
            id = data['id'] 
            


            model_get = post if model=='post' else   Comment.objects.get(post=post, id=id)
            query_action = getattr(model_get, action) 
            print(query_action)
            query_action.remove(request.user) if request.user in  query_action.all() else   query_action.add(request.user) 

        elif action == 'leave_comment':
            text_comment = data['text_comment']
            Comment.objects.create(
                owner=request.user, 
                text=text_comment, 
                post=post,
            ) 
        elif action == 'share': 
            pass
     

    return render(request, 'post/list_post.html') 



class CommentApiView(APIView): 
    def get(self, request, post_id): 
        posts_comment = Comment.objects.filter(post=post_id) 
        paginator = Paginator(posts_comment, 2)  # Show 25 contacts per page.

        page_number = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_number) 
        context = {"replies": page_obj} 
        page_comment = render_to_string("includes/comments_replies.html", context=context, request=request) 
        #sr_data = CommentSerialezers(page_comment).data
        context = {"new_page_comment": page_comment, 'has_next_page': page_obj.has_next()}

        return JsonResponse(context)