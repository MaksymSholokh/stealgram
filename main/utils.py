from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.contrib.auth.models import User 

from users.models import Profile, Friend
from django.db.models import Q


from common.utils import cache_fun



def user_search(query):
    #return User.objects.annotate(search=SearchVector("first_name", "last_name"),).filter(search=query) 
    # vector = SearchVector("first_name", 'last_name', 'username')
    # query = SearchQuery(query)  
    res = cache_fun(f'search_users_{query}', User.objects.filter(first_name__icontains=query), 60)
    
    return res
    # return User.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gt=0).order_by("-rank") 


def list_friends(user): 
    friends = Friend.objects.filter(Q(to_user=user) | Q(from_user=user))
    #return friends
    return  [f.to_user if  f.to_user != user else f.from_user for f in friends  ]