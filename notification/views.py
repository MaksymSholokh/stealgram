from django.shortcuts import render 
from django.contrib.auth import get_user_model
from .models import Notification

from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from rest_framework.generics import RetrieveAPIView
from django.http import HttpResponse, JsonResponse


from .permission import IsOwner 
from .serializers import NotificationSerializer


class NotificationApiView(APIView):  
    renderer_classes = [TemplateHTMLRenderer] 
    permission_classes = [IsOwner] 

    def get(self, request, username):   
        recipient = get_user_model().objects.get(username=username)
        users_notf =  Notification.objects.filter(recipient=recipient.id).order_by('-created')
        content= {'notifications': users_notf} 
        return Response(content, template_name='notification/notfication_list.html')  
    
    def put(self, request, *args, **kwargs): 
        notifs = request.data 

        done_notif = []
        for notif in notifs:  
            id_notif = notif.get('id') 
            obj = Notification.objects.get(id=id_notif)

            serializer = NotificationSerializer(data=notif)  
            if serializer.is_valid():   
            
                serializer.update(obj)   
                done_notif.append(notif)
        return JsonResponse({"keys_changed_notif": done_notif})

                