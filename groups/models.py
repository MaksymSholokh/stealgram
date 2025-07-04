from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth import get_user_model 

user = get_user_model()


class Group(models.Model): 
    name = models.CharField(max_length=50, unique=True) 
    description = models.CharField(max_length=500) 
    photo = models.ImageField(upload_to=f"group_avatar/{name}/{timezone.now().strftime('%Y/%m/%d')}/") 
    created = models.DateTimeField(auto_now=True)


    member = models.ManyToManyField(through='Member', to=user)



class Member(models.Model):  
    class Role(models.TextChoices): 
        admin = 'admin'
        staff = 'staff' 
        follower = 'follower'




    role = models.CharField(choices=Role, default=Role.follower)
    group = models.ForeignKey(Group, related_name='group_member', on_delete=models.CASCADE)
    user = models.ForeignKey(user, related_name='user_group', on_delete=models.CASCADE) 
    



