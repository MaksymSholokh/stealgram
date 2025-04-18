import json

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

from .models import Message, ChatTwoUser
from django.utils import timezone

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope["user"]
        self.room_name = self.scope["url_route"]["kwargs"]["chat_id"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]  

        chat = ChatTwoUser.objects.get(id=int(self.room_name))

        # save message to postgres 
        Message.objects.create(
            chat=chat, 
            owner = self.user, 
            text_message = message,  
            

        )
        now = timezone.now()
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {
                "type": "chat.message", 
                "message": message, 
                'username': self.user.username,
                'datetime': now.isoformat(),
                })

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]
        username = event["username"] 
        

        # Send message to WebSocket
        self.send(text_data=json.dumps(
            {
                "message": message, 
                'username': username,
                })) 


