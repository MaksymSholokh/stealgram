from django import template

register = template.Library()

@register.simple_tag
def find_other_user(chat, user): 
    return chat.other_user(user)