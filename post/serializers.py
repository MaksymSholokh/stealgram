from rest_framework import serializers
from .models import Comment, Post


class CommentSerialezers(serializers.Serializer): 
    text = serializers.CharField() 




class PostChangeSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Post 
        fields = ['text', 'photo', 'video'] 

    def update(self, instance, validated_data):


        instance.text = validated_data.get('text', instance.text)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.video = validated_data.get('video', instance.video)

        instance.save()  
        return instance

