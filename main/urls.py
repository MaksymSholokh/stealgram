from django.urls import path, include  
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.q_search, name='search'),
]
