from .models import Profile 
from django.contrib.auth.models import User 
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=User) 
def create_profile_from_user(sender, instance, created,  **kwargs): 
    if created: 
        Profile.objects.create(user=instance) 

@receiver(post_save, sender=User) 
def save_new_data_profile(sender, instance, **kwargs):
    instance.profile.save()