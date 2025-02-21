from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
# Create your models here.


def user_dir_path(instance, filename):
    return f"{instance.user.username}/{timezone.now().strftime('%Y/%m/%d')}/{filename}"

class Profile(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12) 
    friends = models.ManyToManyField(to='self', symmetrical=True, blank=True, through='Friend') 

    photo = models.ImageField(upload_to=user_dir_path, blank=True, null=True)
    about = models.TextField(max_length=2000, blank=True, null=True) 
    location = models.CharField(max_length=200, blank=True, null=True)


class Friend(models.Model): 
    from_user = models.ForeignKey(User, related_name='from_friend', on_delete=models.CASCADE) 
    to_user = models.ForeignKey(User, related_name='to_friend', on_delete=models.CASCADE) 
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    
        return self.to_user.first_name
    