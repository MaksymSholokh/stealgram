from rest_framework.permissions import BasePermission 
from post.models import Post


class IsOwner(BasePermission):  
    def has_permission(self, request, view): 
        user_data_list = [request.user.username, request.user.id]
        
        user_data = view.kwargs.get('username')  
        if not user_data:
            post_id = view.kwargs.get('post_id')  
            user_data = Post.objects.get(id=post_id).owner.id
        return (user_data in user_data_list and request.user.is_authenticated)



