from django.urls import path, include 
from . import views

app_name = 'chat'

urlpatterns = [
    path('share/', views.share_content, name='share'), 

    path('create/<int:user_id>/', views.create_chat_two_user, name='create_chat_two_users'),
    path('<int:chat_id>/', views.chat_two_user, name='chat_two_users'), 
    path('all-chats/', views.chats, name='all_chats'), 


]
