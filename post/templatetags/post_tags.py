from itertools import chain
from django import template
from django.db.models import Count 
from post.models import Post

register = template.Library() 



@register.simple_tag
def order_comment(posts, user):  
    #comment = Comment.objects.get(post=post, id=comment_id) 

    users_comments = posts.filter(owner=user).order_by('-created')   
    other_comments = posts.annotate(count_like=Count('like')).order_by('-count_like', '-created').exclude(owner=user) 

    all_comments =  list(chain(users_comments, other_comments))  
    return all_comments