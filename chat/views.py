from django.shortcuts import redirect, render
from .models import ChatTwoUser, Message
from django.db.models import Q, Max, Count
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
import base64 

# Create your views here.



@login_required(login_url='users:login')
def create_chat_two_user(request, user_id):  
    first_user = request.user
    second_user = User.objects.get(id=user_id)
    
    if first_user.id > second_user.id: 
        first_user, second_user = second_user, first_user

    chat, created = ChatTwoUser.objects.get_or_create(first_user=first_user, second_user=second_user) 

    return redirect('chat:chat_two_users', chat_id=chat.id) 



@login_required(login_url='users:login')
def chat_two_user(request, chat_id):  

    chat = ChatTwoUser.objects.get(id=chat_id) 

    try:
        histori_chat = Message.objects.filter(chat=chat).order_by('created')
    except: 
        histori_chat = None   
    
        
    context = {
        'chat_id': chat_id,
        'chat': chat,
        'histori_chat': histori_chat, 
        }
    return render(request, 'chat/chat_page.html', context=context)


@login_required(login_url='users:login')
def chats(request): 

    chats = ChatTwoUser.objects.filter(
        Q(first_user=request.user)|Q(second_user=request.user)
        )
    unread_chats = chats.filter(messages__is_read=False, messages__receiver=request.user).distinct().order_by('-created') 
    other_chats = chats.exclude(id__in=unread_chats.values('id')).distinct().order_by('-created')  

    chats_and_user = []
    for chats in unread_chats: 
        other_user = chats.other_user(request.user) 
        count_unread_message = chats.messages.filter(is_read=False).count()
        last_message_in_chat = chats.messages.latest('created')
        chats_and_user.append({
            'chats': chats,
            'other_user': other_user, 
            'last_message_in_chat': last_message_in_chat.text_message, 
            'count_unread_message': count_unread_message})

  
 
    another_chats_and_users = [] 
    
    for chat in other_chats:  
        try:
            last_message_in_chat = chat.messages.latest('created')  
            last_user = last_message_in_chat.sender 
        except: 
            last_message_in_chat = 'No message yet' 
            last_user = chat.other_user
        another_chats_and_users.append({
            'chat':  chat, 
            'last_message_in_chat': last_message_in_chat.text_message, 
            'last_user': last_user})


    context = {'another_chats_and_users': another_chats_and_users, 'chats_and_user': chats_and_user} 
    return render(request, 'chat/all_chats.html', context)