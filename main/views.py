from django.shortcuts import render
from .utils import user_search, list_friends
from django.contrib.auth.models import User 
from users.models import Profile, Friend
from django.contrib.auth.decorators import login_required 



# Create your views here.
 




def index(request): 
    
    return render(request, 'main/index.html') 

@login_required(login_url='users:login')
def q_search(request): 
    query = request.GET.get('q') 

    search = user_search(query)#.exclude(id=request.user.id) 


    friends = list_friends(request.user) 
    
    context = {"search": search, 'friends': friends} 
    return render(request, 'main/search.html', context=context) 



