from django.shortcuts import get_object_or_404
from .models import Profile 
from django.contrib.auth.models import User 




def user_without_username(user_data):  
    user_name = user_data['username']

    try:
        User.objects.get(username=user_name)
        return user_name 
    except:
        if ''.join(filter(lambda x: ord(x) >= 65 or x in ['.', '@', '_'], user_name)): 
            user = User.objects.get(email=user_name) 
        else: 
            profile = Profile.objects.get(phone_number=user_name)  
            user = profile.user
        return user.username