from django.urls import path
from . import views

app_name = 'post' 


urlpatterns = [
    #path('create-post/', views.create_post, name='create_post'),  
    #path('comment/page/<int:post_id>/', views.commmnet_page, name='comment_page'),
    path('list-post/<slug:username>/', views.list_post, name='list_posts'),  
    path('<int:post_id>/', views.post, name='post'), 
    path('comment/<int:post_id>/', views.CommentApiView.as_view(), name='comment'), 
    path('change-post/<int:post_id>/', views.ChangePostApi.as_view(), name='change_post'),
    

]
