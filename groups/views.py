from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from .models import Group, Member

from django.db.models import Q

from .permissions import GroupPermissions
from rest_framework import permissions




class AllGroups(APIView): 


    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'groups/list_group.html'
    permission_classes = [GroupPermissions, permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):  
        user = request.user
        groups_staff = Group.objects.filter(group_member__user=user, group_member__role__in=[Member.Role.admin, Member.Role.staff]) 
        followed_groups = Group.objects.filter(group_member__user=user, group_member__role=Member.Role.follower)  

        context = {'follow_groups': followed_groups, 'manage_groups': groups_staff} 
        return Response(context)

    def post(self, request): 
        pass 

class GroupObj(APIView): 
    def get(self, request, *args, **kwargs): 
        return Response({'ok': 'ok'})