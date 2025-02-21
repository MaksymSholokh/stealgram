from django.db import models
from django.contrib.auth.models import User 
from users.models import user_dir_path
# Create your models here.



class Published(models.Manager): 
    def get_queryset(self):
        return super().get_queryset().filter(status="Pb")
    


class Post(models.Model): 
    STATUS_CHOICES = [
    ("Pb", "Published"),
    ("Dr", "Draft"),
    ]


    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user') 
    create_time= models.DateTimeField(auto_now_add=True) 
    rewrite_time = models.DateTimeField(auto_now=True) 
    text = models.TextField(max_length=10000) 
    photo = models.ImageField(upload_to=user_dir_path, blank=True, null=True) 
    video = models.FileField(upload_to=user_dir_path,  blank=True, null=True) 
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='Dr')

    objects = models.Manager() 
    published = Published() 


class Comment(models.Model): 
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner') 
    created = models.DateTimeField(auto_now_add=True) 
    text = models.TextField(max_length=100) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='owner') 
