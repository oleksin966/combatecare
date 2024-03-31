from django.urls import path
from .views import item_list, item_detail

urlpatterns = [
    path('', item_list, name='home'),
    path('item/<str:slug>/', item_detail, name='item_detail'),
]