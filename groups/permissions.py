from rest_framework import permissions

from .models import Member, Group

class GroupPermissions(permissions.BasePermission): 
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True 
        
        elif request.method == "POST": 
            pass