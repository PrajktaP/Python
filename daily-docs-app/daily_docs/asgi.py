import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from tasks import consumers  # Assuming you will create consumers for handling WebSocket connections

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'daily_docs.settings')
django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            [
                # path('ws/some_path/', consumers.YourConsumer.as_asgi()),  # Add your WebSocket URL patterns here
            ]
        )
    ),
})