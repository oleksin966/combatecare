from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.backends.db import SessionStore
#from .models import Cart, CartItem
from warehouse.models import Item
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
import json

from .cart import Cart
from warehouse.models import Item

def get_cart_item_data(cart_items):
    return [{
        'id': cart_item["item"].id,
        'name': cart_item["item"].name,
        'quantity': cart_item["quantity"],
        'max_quantity': cart_item["item"].quantity,
        'photo': str(cart_item["item"].photo.url) if cart_item["item"].photo else '',
    } for cart_item in cart_items]

def add_to_cart(request, item_id):
    cart = Cart(request)
    cart.add(item_id)
    item = get_object_or_404(Item, pk=item_id)
    cart_items = cart.get_cart_items()
    response_data = {'message': 'ok', 'cart_items': get_cart_item_data(cart_items)}
    return JsonResponse(response_data)

def remove_from_cart(request, item_id):
    cart = Cart(request)
    cart.remove(item_id)
    cart_items = cart.get_cart_items()
    response_data = {'message': 'ok', 'cart_items': get_cart_item_data(cart_items)}
    return JsonResponse(response_data)

def cart_detail(request):
    cart = Cart(request)
    cart_items = cart.get_cart_items()
    response_data = {'message': 'ok', 'cart_items': get_cart_item_data(cart_items)}
    return JsonResponse(response_data)

def cart_update_quantity(request, item_id):
    data = json.loads(request.body)
    quantity_key = f"quantity_{item_id}"
    quantity = data.get('quantity', 1)
    cart = Cart(request)
    cart.update_quantity(item_id, quantity)
    cart_items = cart.get_cart_items()
    response_data = {'message': 'ok', 'cart_items': get_cart_item_data(cart_items)}
    return JsonResponse(response_data)

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return JsonResponse({'message': 'ok', 'cart_items':[]})













# def add_to_cart(request, item_id):
#     cart = Cart(request)
#     cart.add(item_id)
#     item = get_object_or_404(Item, pk=item_id)
#     return JsonResponse({'message':'ok'})

# def remove_from_cart(request, item_id):
#     cart = Cart(request)
#     cart.remove(item_id)
#     #print(cart.get_cart_items())
#     return redirect('/')
#     #return JsonResponse({'message':'removed'})

# def cart_detail(request):
#     cart = Cart(request)
#     cart_items = cart.get_cart_items()
#     return render(request, 'cartitems.html', {'cart': cart, 'cart_items': cart_items})

# def add_to_cart(request, slug):
#     item = get_object_or_404(Item, slug=slug)
#     cart_id = request.session.get('cart_id')
#     if cart_id:
#         cart = Cart.objects.get(id=cart_id)
#     else:
#         if request.user.is_authenticated:
#             cart = Cart.objects.filter(user=request.user).first()
#         else:
#             cart = Cart.objects.filter(user=None).first()
#             if not cart:
#                 cart = Cart.objects.create(user=None)
#         request.session['cart_id'] = cart.id

#     #cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
#     cart_item_query = CartItem.objects.filter(item=item, cart=cart)
#     if cart_item_query.exists():
#         cart_item, created = cart_item_query.first(), False
#     else:
#         cart_item, created = CartItem.objects.create(item=item, cart=cart), True
#     #print(cart_item)
#     if not created:
#         cart_item.quantity += 1
#         cart_item.save()
#     return JsonResponse({'message':'OK'})

# def cart_detail(request):
#     cart_id = request.session.get('cart_id')
#     if cart_id:
#         cart = Cart.objects.get(id=cart_id)
#         print(cart)
#     else:
#         cart = None
#         print(cart)
#     return render(request, 'cartitem.html', {'cart': cart})



#c = Cart.objects.all()



#print(dir(c[1]))
#print(c[1].items.all().values_list())







#print(dir(c[1].items))
# def remove_from_cart(request, slug):
#     cart_id = request.session.get('cart_id')
#     if cart_id:
#         cart = Cart.objects.get(id=cart_id)
#         cart_item = get_object_or_404(CartItem, cart=cart, slug=slug)
#         cart_item.delete()
#     return JsonResponse({'message':'REMOVED'})
#cart_item = CartItem.objects.filter(item=item, cart=cart).first()