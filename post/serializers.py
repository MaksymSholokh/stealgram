from rest_framework import serializers
from .models import Comment


class CommentSerialezers(serializers.Serializer): 
    text = serializers.CharField()