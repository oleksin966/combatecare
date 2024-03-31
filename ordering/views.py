from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order
from cartitem.cart import Cart
from django.utils import timezone
from datetime import datetime
from accounts.models import CustomUser, Deliveryman
from django.db.models import Q
import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404

@login_required
def create_order(request):
    user = request.user
    cart = request.session.get('cart', {})
    date = timezone.now()

    items_json = json.dumps(cart)

    try:
        military = CustomUser.objects.get(username=user.username)
    except CustomUser.DoesNotExist:
        military = None
    if (cart != {} and hasattr(user, 'military')):
        order = Order.objects.create(
            military=military,
            items=items_json,
            date_order=date,
            delivery_location='',
            volunteer=None,
            status='not_confirmed'
        )
        request.session['cart'] = {}
        return redirect('user_orders', order_id=order.id)
    return redirect('home')


@login_required
def get_all_orders(request):
    orders = Order.objects.all()
    orders_data = []

    for order in orders:
        order_data = {
            'id': order.id,
            'military': order.military.username if order.military else None,
            'items': json.loads(order.items),
            'date_order': order.date_order,
            'delivery_location': order.delivery_location,
            'volunteer': order.volunteer.username if order.volunteer else None,
            #'date_arrival': order.date_arrival.isoformat() if order.date_arrival else None,
            'status': order.status,
        }
        orders_data.append(order_data)

    return JsonResponse({'orders': orders_data})

@login_required
def user_orders(request, order_id):
    order = Order.objects.get(id=order_id)
    context = {'orders': []}
    if order.status == "not_confirmed":
        parsed_items = parse_order_items(order.items)
        order_data = {
            'id': order.id,
            'date_order': order.date_order,
            'status': order.status,
            'items': parsed_items
        }
        context = {'order': order_data, 'user': request.user}
    return render(request, 'user_orders.html', context)


def parse_order_items(items):
    items_dict = json.loads(items)
    parsed_items = []
    for item_id, item_data in items_dict.items():
        parsed_item = {
            'id': item_id,
            'name': item_data['name'],
            'slug': item_data['slug'],
            'description': item_data['description'],
            'photo': item_data['photo'],
            'quantity': item_data['quantity']
        }
        parsed_items.append(parsed_item)
    return parsed_items

def send_to_approval(request, order_id):
    data = json.loads(request.body)

    order_id = data['order_id']
    latitude = data['latitude']
    longitude = data['longitude']
    adress = data['adress']

    order = Order.objects.get(id=order_id)

    order.delivery_location = adress
    order.delivery_latitude = latitude
    order.delivery_longitude = longitude
    order.status = 'is_expected'
    #print(order.__dict__)
    order.save()

    return JsonResponse({'message': 'ok'})

def pending_approval(request, order_id):
    order = Order.objects.get(id=order_id)
    deliverymans = Deliveryman.objects.filter(status='Вільний')
    order_data = {
        'id': order.id,
        'military': order.military if order.military else None,
        'items': json.loads(order.items),
        'date_order': order.date_order,
        'delivery_location': order.delivery_location,
        'delivery_latitude': order.delivery_latitude,
        'delivery_longitude': order.delivery_longitude,
        'volunteer': order.volunteer.username if order.volunteer else None,
        'status': order.status,
        'date_departure': order.date_departure,
        'time_departure': order.time_departure,
    }
    context = {'order': order_data, 'deliverymans': deliverymans}
    return render(request, 'pending_approval.html', context)

def approved_order(request, order_id):
    order = Order.objects.get(id=order_id)
    data = json.loads(request.body)
    deliveryman = CustomUser.objects.get(username=data["deliveryman"])
    order.deliveryman = deliveryman

    date_str = data['departure_date']
    time_str = data['departure_time']
    date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
    time_obj = datetime.strptime(time_str, '%H:%M').time()

    order.date_departure = date_obj
    order.time_departure = time_obj

    order.volunteer = request.user
    order.status = "confirmed"

    order.save()

    return JsonResponse({'message': 'ok'})


def cancel_order(request, order_id):
    order = Order.objects.get(id=order_id)
    data = json.loads(request.body)

    order.status = "canceled"
    order.save()
    return JsonResponse({'message': 'ok'})

@login_required
def get_orders_by_status(request, status):
    #status_key = dict(Order.status.field.choices)[status]
    if hasattr(request.user, 'military'):
        orders = Order.objects.filter(Q(status=status) & Q(military=request.user))
    elif hasattr(request.user, 'volunteer'):
        orders = Order.objects.filter(status="is_expected")
    elif hasattr(request.user, 'deliveryman'):
        orders = Order.objects.filter(status=status, deliveryman=request.user)
    orders_list = []
    for order in orders:
        orders_list.append({
            'id': order.id,
            'military': order.military.username,
            'items': parse_order_items(order.items),
            'delivery_location': order.delivery_location,
            'deliveryman': order.deliveryman.username if order.deliveryman else '',
            'volunteer': order.volunteer.username if order.volunteer else '',
            'date_order': order.date_order.strftime('%Y-%m-%d %H:%M:%S'),
            'status': order.status,
            'date_departure': order.date_departure.strftime('%Y-%m-%d') if order.date_departure else '',
            'time_departure': order.time_departure.strftime('%H:%M:%S') if order.time_departure else '',
        })
    return JsonResponse({'orders': orders_list})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    items = parse_order_items(order.items)
    context = {'order': order,
               'items': items,
                }
    return render(request, 'order_details.html', context)