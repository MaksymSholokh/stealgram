from celery import shared_task
from .models import Notification
from django.contrib.auth.models import User

@shared_task
def new_post_notification(recipient, message): 
    user = User.objects.get(id=recipient)
    return Notification.objects.create(recipient=user, message=message) 



# start celery + rabbit
#celery -A stealgram worker --loglevel=INFO  
#sudo rabbitmq-server


