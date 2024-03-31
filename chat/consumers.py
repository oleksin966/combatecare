import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from accounts.models import CustomUser
from .models import Message, Chat
from django.core import serializers
from django.http import QueryDict
from datetime import datetime

 
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        sender_username = self.scope["user"].username
        recipient_username = self.scope["url_route"]["kwargs"]["room_name"]
        usernames = sorted([sender_username, recipient_username])
        self.room_group_name = f"chat_{usernames[0]}_{usernames[1]}"

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()


    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get("message", "")
        author = text_data_json.get("author", self.scope["user"].username)
        recipient_username = self.scope["url_route"]["kwargs"]["room_name"]

        chat = Chat.objects.filter(users=self.scope['user']).filter(users__username=recipient_username).first()
        if not chat:
            chat = Chat.objects.create()
            chat.users.add(self.scope['user'], CustomUser.objects.get(username=recipient_username))
        
        if message:
            message_ = Message.objects.create(
                chat=chat,
                sender=self.scope['user'],
                recipient=CustomUser.objects.get(username=recipient_username),
                text=message,
                timestamp=datetime.now()
            )

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message, "author": author}
        )


    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]
        message_type = event["type"]
        author = event["author"]

        self.send(text_data=json.dumps({"message": message, "type": message_type, "author": author}))
















