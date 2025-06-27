from rest_framework.permissions import BasePermission 

class IsOwner(BasePermission):  
    def has_permission(self, request, view):
        username = view.kwargs.get('username')  
        return (request.user.username == username and request.user.is_authenticated)



