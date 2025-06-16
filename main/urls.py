from django.urls import path, include  
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.q_search, name='search'), 

    path('ask/', views.AskGeminiApi.as_view(), name='ask'),

    path('api/all-posts/', views.AllPostsView.as_view()),
    path('api/post/<int:pk>/', views.OnePostView.as_view()),
    path('api/create-post/', views.TestPostView.as_view()),
]
