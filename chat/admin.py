from django.contrib import admin
from .models import Chat, Message

class ChatAdmin(admin.ModelAdmin):
    list_display = ('id', 'display_users', 'display_sender', 'display_recipient')

    def display_users(self, obj):
        return ", ".join([user.username for user in obj.users.all()])

    display_users.short_description = 'Users'

    def display_sender(self, obj):
        return obj.messages.first().sender.username if obj.messages.first() else '-'

    display_sender.short_description = 'Sender'

    def display_recipient(self, obj):
        return obj.messages.first().recipient.username if obj.messages.first() else '-'
    
    display_recipient.short_description = 'Recipient'

admin.site.register(Chat, ChatAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display = ('text', 'sender', 'recipient', 'timestamp')

admin.site.register(Message, MessageAdmin)