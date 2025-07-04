from django.urls import path
from .views import *


app_name = 'groups'

urlpatterns = [
    path('all-groups/', AllGroups.as_view(), name='all_group'),  

    path('<slug:group_name>/', GroupObj.as_view(), name='group_name'),
]