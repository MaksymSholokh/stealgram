from django import forms  
from django.contrib.auth.forms import PasswordResetForm
from .models import Profile
from django.contrib.auth.models import User

import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type 




class AuthenticationForm(forms.Form): 
    username = forms.CharField() 
    password = forms.CharField(widget=forms.PasswordInput)  
    class Meta: 
        model = User 
        fields =  ['username', 'password'] 





class RegisterUserForm(forms.ModelForm): 
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput) 

    class Meta: 
        model = User  
        fields = ['username',  'email']

    def clean_password2(self): 
        cd_password = self.cleaned_data['password'] 
        cd_password2 = self.cleaned_data['password2'] 

        if cd_password != cd_password2: 
            raise  forms.ValidationError('diferent password')
        return cd_password2






class RegisterProfileFrorm(forms.ModelForm):
    phone_number = forms.CharField()  

    class Meta: 
        model = Profile 
        fields = ['phone_number'] 

    def clean_phone(self): 
        cd = self.cleaned_data['phone_number']
        number_validator = carrier._is_mobile(number_type(phonenumbers.parse(cd)))
        if number_validator: 
            return cd 
        else: 
            raise forms.ValidationError('Not valid number') 
        


class CustomePasswordResetForm(PasswordResetForm): 
    username = forms.CharField() 
    #email = forms.EmailField() 

    def clean(self):  
        cd = self.cleaned_data
        username = cd['username']  
        email = cd['email']  

        user = User.objects.filter(username=username, email=email).first()
        if not user: 
            raise  forms.ValidationError('not found user with this email') 
        return cd 
