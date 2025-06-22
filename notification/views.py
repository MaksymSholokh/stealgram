from django.shortcuts import render 
from django.contrib.auth import get_user_model
from .models import Notification

from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from rest_framework.generics import RetrieveAPIView

class NotificationApiView(APIView):  
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, username):   
        recipient = get_user_model().objects.get(username=username)
        users_notf =  Notification.objects.filter(recipient=recipient.id).order_by('-created')
        content= {'notifications': users_notf} 
        return Response(content, template_name='notification/notfication_list.html')  
    
    
    


    