# views.py

from django.shortcuts import render
from .models import Chat, Message
from accounts.models import CustomUser
from django.http import JsonResponse
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def init_chat(request):
    user = request.user
    usernames = CustomUser.objects.exclude(pk=user.pk)
    return render(request, 'chatroom.html', {"usernames": usernames})

@login_required
def get_messages(request, room_name):
    chat = Chat.objects.filter(users=request.user).filter(users__username=room_name).first()
    messages = list(chat.messages.values('text', 'sender'))
    return JsonResponse(messages, safe=False)

@login_required
def search_users(request):
    query = request.GET.get('query', '')
    if query and len(query) < 2:
        return JsonResponse({'error': 'Query must be at least 2 characters long'})

    if query:
        users = CustomUser.objects.filter(
            Q(username__icontains=query) |
            Q(email__icontains=query) |
            Q(phone__icontains=query),
            is_active=True,
        )
    else:
        users = CustomUser.objects.filter(is_active=True)
    data = {
        'users': [{'id': user.id, 'username': user.username } for user in users]
    }

    return JsonResponse(data)

@login_required
def chat(request, room_name):
    user = request.user
    chats = Chat.objects.filter(users=user)
    usernames = CustomUser.objects.exclude(pk=user.pk)
    recipient = CustomUser.objects.get(username=room_name)
    phone_number = recipient.phone

    if hasattr(recipient, 'volunteer'):
        role = 'Волонтер'
    elif hasattr(recipient, 'deliveryman'):
        role = 'Доставщик'
    elif hasattr(recipient, 'military'):
        role = 'Військовий'
    else:
        role = 'Адмін'

    context = {
        "chats": chats, 
        "usernames": usernames, 
        "room_name": room_name, 
        "phone": phone_number,
        "role": role
    }
    return render(request, 'chatroom.html', context)






