from django.dispatch import receiver
from post.models import Post, Comment 

from django.db.models.signals import post_save 



@receiver(post_save, sender=Post)
def notifacation_new_like(sender, instance, created, **kwargs): 
    if created: 
        pass



