import json
import uuid
from django.core.files.base import ContentFile

import base64 

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth import get_user_model
from .models import Message, ChatTwoUser



class ChatConsumer(WebsocketConsumer):
    def connect(self):
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
        content = text_data_json["content"] 

        show_content = None
        image = None
        if content != 'None':  
            show_content = f"data:image/jpeg;base64,{content}" 
            image = ContentFile(base64.b64decode(content), name=f"{uuid.uuid4()}.png")


        user = get_user_model().objects.get(username = self.scope['user'])  
        chat = ChatTwoUser.objects.get(id=int(self.room_name)) 
        receiver_user = chat.second_user if chat.first_user == user else  user

        create_message = Message.objects.create(
            chat=chat, 
            sender=user,  
            receiver = receiver_user,
            text_message=message, 
            photo=image
            )
        # create_message = Message.objects.get(owner=user, chat=chat)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat.message", "message": message, 'owner': user.id, 'time': create_message.created.isoformat(), 'content': show_content}
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]
        owner = event['owner'] 
        time = event['time']  
        content = event['content']
        chat = int(self.scope["url_route"]["kwargs"]["chat_id"])


        Message.objects.filter(chat=chat, is_read=False, receiver=owner).update(is_read=True)


        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message, 'owner': owner, 'time': time, 'content': content}))
