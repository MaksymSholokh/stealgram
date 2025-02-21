from django.shortcuts import redirect, render
from .models import ChatTwoUser, Message, MessageReadStatus
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.



@login_required
def create_chat_two_user(request, user_id):  
    first_user = request.user
    second_user = User.objects.get(id=user_id)
    
    if first_user.id > second_user.id: 
        first_user, second_user = second_user, first_user

    chat, created = ChatTwoUser.objects.get_or_create(first_user=first_user, second_user=second_user) 

    return redirect('chat:chat_two_users', chat_id=chat.id) 


@login_required
def chat_two_user(request, chat_id): 
    chat = ChatTwoUser.objects.get(id=chat_id) 

    try:
        histori_chat = Message.objects.filter(chat=chat).order_by('-created')

    except: 
        histori_chat = None  
    page_obj = None 

    page_number = request.GET.get("page", 1)

    if histori_chat.exists():
        paginator = Paginator(histori_chat, 15)  # Show 25 contacts per page.

        page_obj = paginator.get_page(page_number)


    context = {'chat_id': chat_id, 'histori_chat': histori_chat, 'page_obj': page_obj}
    return render(request, 'chat/chat_page.html', context=context)
