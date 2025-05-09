from django import forms 
from .models import ChatTwoUser, Message



class PhotoChat(forms.ModelForm): 
    class Meta: 
        model = Message 
        fields = ['photo'] 


