from post.models import Post 
from rest_framework import serializers


class AllPostsSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Post 
        fields = ['id', 'text']  


class DeletePost(serializers.Serializer): 
    id = serializers.IntegerField() 
    text = serializers.CharField(required=False)








class TemplateGeminiSerializer(serializers.Serializer): 
    user_id = serializers.IntegerField(required=False) 
    promt = serializers.CharField() 
    extra_info = serializers.CharField(required=False, allow_blank=True)






