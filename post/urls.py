from django.urls import path
from . import views

app_name = 'post' 


urlpatterns = [
    #path('create-post/', views.create_post, name='create_post'), 
    path('list-post/<slug:username>/', views.list_post, name='list_posts'),  
    path('<int:post_id>/', views.post, name='post'),
    

]
