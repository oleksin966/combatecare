from django.urls import path
from .views import chat, init_chat, search_users, get_messages

urlpatterns = [
    path("chat/", init_chat, name="init_chat"),
    path("chat/<str:room_name>/", chat, name="chat"),
    path("search_users/", search_users, name='search_users'),
    path("get_messages/<str:room_name>/", get_messages, name="get_messages")
]