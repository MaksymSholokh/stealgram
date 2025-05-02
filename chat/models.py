from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
# Create your models here.



class ChatTwoUser(models.Model): 
    first_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='first_user')
    second_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='second_user') 
    created = models.DateTimeField(auto_now_add=True)  


    def other_user(self, owner):  
        other_user = self.second_user if self.first_user == owner else self.first_user
        return other_user


class Message(models.Model): 
    chat = models.ForeignKey(ChatTwoUser, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender_user', null=True) 
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver_user', null=True)
    text_message = models.TextField(max_length=1000, blank=True, null=True) 
    photo = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True) 
    is_read = models.BooleanField(default=False) 
