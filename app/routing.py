from django.urls import re_path
from app.consumers import UserConsumer

websocket_urlpatterns = [
    re_path(r'ws/users/$', UserConsumer.as_asgi()),
]
