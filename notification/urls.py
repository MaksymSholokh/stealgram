
from django.urls import path, include 
from . import views



app_name = 'notification'

urlpatterns = [
    path('<slug:username>/', views.NotificationApiView.as_view(), name='username')

] 
