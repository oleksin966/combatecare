from django.urls import path
from .views import task_detail, start_move, mark_as_delivered, update_driver_location

urlpatterns = [
    path('delivering/order/<int:order_id>/', task_detail, name='task_detail'),
    path('delivering/move/<int:order_id>', start_move, name='start_move'),
    path('delivering/delivered/<int:order_id>', mark_as_delivered, name='mark_as_delivered'),
    path('delivering/update/location/<int:order_id>', update_driver_location, name='update_driver_location'),

]
