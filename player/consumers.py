import json

from channels.generic.websocket import AsyncWebsocketConsumer


class PlayerConsumer(AsyncWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.library_id = None
        self.player_group_name = None

    async def connect(self):
        self.library_id = self.scope["url_route"]["kwargs"]["library_id"]
        self.player_group_name = f"player_{self.library_id}"

        await self.channel_layer.group_add(self.player_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.player_group_name, self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        await self.channel_layer.group_send(
            self.player_group_name, {"type": "chat.message", "message": message}
        )

    async def chat_message(self, event):
        message = event["message"]

        await self.send(text_data=json.dumps({"message": message}))