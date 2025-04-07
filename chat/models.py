from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
# Create your models here.



class ChatTwoUser(models.Model): 
    first_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='first_user')
    second_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='second_user') 
    creted = models.DateTimeField(auto_now_add=True)


class Message(models.Model): 
    chat = models.ForeignKey(ChatTwoUser, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text_message = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True) 
    is_read = models.BooleanField(default=False)