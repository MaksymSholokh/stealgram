"""
ASGI config for stealgram project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from chat.routing import websocket_urlpatterns as chat_websocket_urlpatterns
from notification.routing import websocket_urlpatterns as notification_websocket_urlpatterns


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stealgram.settings')


all_websocket_urlpatterns = notification_websocket_urlpatterns + chat_websocket_urlpatterns

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(all_websocket_urlpatterns))
        ),
    # Just HTTP for now. (We can add other protocols later.)
})


