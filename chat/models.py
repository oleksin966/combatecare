from django.db import models
from accounts.models import CustomUser

class Chat(models.Model):
    users = models.ManyToManyField(CustomUser, related_name='chats')

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чати'


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_messages')
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Повідомлення'
        verbose_name_plural = 'Повідомлення'