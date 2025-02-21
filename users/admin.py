from django.contrib import admin
from django.urls import reverse 
from .models import Profile, Friend
from django.utils.html import format_html


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'user_link'] 
    search_fields = ['user__username']
    

    def user_link(self, obj): 
        url = reverse('admin:auth_user_change', args=[obj.user.id])
        return format_html('<a href="{}">{}</a>', url, obj.user.username)


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin): 
    list_display = ['from_user']


  

