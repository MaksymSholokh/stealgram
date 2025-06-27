from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Notification 
        fields = ['id'] 



    def update(self, instance):
        instance.is_read = True 
        instance.save()
        return instance 

