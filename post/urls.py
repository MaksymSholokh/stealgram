from django.urls import path
from . import views

app_name = 'post' 


urlpatterns = [
    path('create-post/', views.create_post, name='create_post'), 
    path('list-post/<int:user_id>', views.list_post, name='list_post'), 

]
