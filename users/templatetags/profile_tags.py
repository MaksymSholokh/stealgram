
from django import template 
from main.utils import list_friends

register = template.Library() 


@register.simple_tag 
def count_friends(user): 
    return len(list_friends(user))


# @register.simple_tag 
# def count_posts(user): 
#     return 