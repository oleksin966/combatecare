from django.urls import path
from . import views

urlpatterns = [
    path('cart/add/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:item_id>/', views.cart_update_quantity, name='cart_update_quantity'),
    path('cart/clear/', views.cart_clear, name='cart_clear'),
    path('cart/', views.cart_detail, name='cart_detail'),
]
