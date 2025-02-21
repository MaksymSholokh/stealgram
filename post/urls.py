from django.urls import path
from . import views

app_name = 'post' 


urlpatterns = [
    path('create-post/', views.create_post, name='create_post'),
]
