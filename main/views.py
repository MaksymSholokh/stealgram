import io
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .utils import user_search, list_friends
from django.contrib.auth.models import User 
from users.models import Profile, Friend
from django.contrib.auth.decorators import login_required 

from .serializers import AllPostsSerializer, DeletePost, TemplateGeminiSerializer
from rest_framework import generics
from post.models import Post 
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from stealgram.settings import GEMINI_API_KEY
from google import genai

class AllPostsView(generics.ListAPIView): 
    queryset = Post.objects.all()
    serializer_class = AllPostsSerializer 


class OnePostView(generics.RetrieveAPIView): 
    queryset = Post.objects.all()
    serializer_class = AllPostsSerializer 


# class CreatePostView(generics.ListCreateAPIView):  
#     queryset = Post.objects.all().order_by('-id')
#     serializer_class = AllPostsSerializer  

class TestPostView(APIView): 
    queryset_p = Post.objects.all().order_by('-id')[:5] 

    def get(self, request): 
        ser_data = DeletePost(self.queryset_p, many=True)
        return Response( ser_data.data) 
    
    def post(self, request): 
        obj = DeletePost(data=request.data) 
        

        if obj.is_valid():  
            sd = obj.data.get('id') 
            Post.objects.get(id=sd).delete()  
            v = Post.objects.all().order_by('-id')[:5]
            popp =  DeletePost(v, many=True)


            return Response(popp.data) 
        return Response(obj.error_messages) 
    
    

    
  
    









def index(request): 
    
    return render(request, 'main/index.html') 

@login_required(login_url='users:login')
def q_search(request): 
    query = request.GET.get('q') 

    search = user_search(query)#.exclude(id=request.user.id) 


    friends = list_friends(request.user) 
    
    context = {"search": search, 'friends': friends} 
    return render(request, 'main/search.html', context=context) 


class AskGeminiApi(APIView):  


    def post(self, request): 
        obj = TemplateGeminiSerializer(data=request.data) 
        if obj.is_valid():  
            answer = obj['promt'] 
            client = genai.Client(api_key=GEMINI_API_KEY)

            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=f"answer the next question use curent language: {answer.value}",
            ) 


            
            return JsonResponse({'ans': response.text})

        
