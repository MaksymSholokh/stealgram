# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/notification/(?P<username>[a-zA-Z]+)/$", consumers.NotificationConsumer.as_asgi()),
]