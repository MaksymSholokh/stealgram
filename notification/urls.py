
from django.urls import path, include 
from . import views



app_name = 'notification'

urlpatterns = [
    path('', views.NotificationApiView.as_view(), name='users_new')

] 
