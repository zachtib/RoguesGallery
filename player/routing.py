from django.urls import re_path

from . import consumers
base64_pattern = r'(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$'
websocket_urlpatterns = [
    re_path(r"ws/player/(?P<library_id>[A-Za-z0-9\-]+)/", consumers.PlayerConsumer.as_asgi()),
]