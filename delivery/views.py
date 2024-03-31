from django.shortcuts import render, get_object_or_404
from ordering.models import Order
from ordering.views import parse_order_items
from django.http import JsonResponse
from django.db.models import Q
import json
from django.utils import timezone

def task_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, deliveryman=request.user)
    order.items = parse_order_items(order.items)
    context = {
        'order': order,
    }
    if request.method == 'POST':
        order.status = 'in_transit'
        order.save()
        return JsonResponse({'success': True})
    return render(request, 'task_detail.html', context)

def start_move(request, order_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        order = Order.objects.get(id=order_id)
        order.status = "in_transit"
        order.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def mark_as_delivered(request, order_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        status = data.get('status')

        order = get_object_or_404(Order, id=order_id)
        order.status = "delivered"
        order.date_arrival = timezone.now()
        order.save()

        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def update_driver_location(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        data = json.loads(request.body)
        order.driver_latitude = data.get('driver_latitude')
        order.driver_longitude = data.get('driver_longitude')
        order.save()
        return JsonResponse({'status': 'Успіх'})
    else:
        return JsonResponse({'status': 'Невдача'})



