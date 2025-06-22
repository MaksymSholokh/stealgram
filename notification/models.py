from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.



class Notification(models.Model): 
    recipient = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, related_name='users_notification_recipient') 
    message = models.CharField(max_length=200) 
    is_read = models.BooleanField(default=False) 
    created = models.DateTimeField(auto_now_add=True)