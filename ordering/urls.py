from django.urls import path
from .views import user_orders, create_order, send_to_approval, pending_approval, get_all_orders, approved_order, cancel_order, get_orders_by_status, order_detail
urlpatterns = [
    path('ordering/create', create_order, name='ordering'),
    path('ordering/user_orders/<int:order_id>', user_orders, name='user_orders'),
    path('ordering/sendapproval/<int:order_id>', send_to_approval, name='send_to_approval'),
    path('ordering/pending_approval/<int:order_id>', pending_approval, name='pending_approval'),
    path('ordering/all', get_all_orders, name='get_all_orders'),
    path('ordering/approved/<int:order_id>', approved_order, name='approved_order'),
    path('ordering/cancel/<int:order_id>', cancel_order, name='cancel_order'),
    path('ordering/status/<str:status>/', get_orders_by_status, name='get_orders_by_status'),
    path('ordering/order_detail/<int:order_id>/', order_detail, name='order_detail'),
    
]