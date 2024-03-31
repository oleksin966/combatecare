from django.conf import settings
from warehouse.models import Item
from django.forms.models import model_to_dict

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, item_id):
        item = Item.objects.get(id=item_id)
        if item_id not in self.cart:
            self.cart[str(item.id)] = {'id': item.id, 'quantity': 0, 'slug': item.slug, 'name': item.name, 'description': item.description,
             'photo': item.photo.url if item.photo else '', }
        self.cart[str(item.id)]['quantity'] += 1
        self.save()

    def remove(self, item_id):
        item_id = str(item_id)
        if item_id in self.cart:
            del self.cart[item_id]
            self.save()
            print(f"Item with ID {item_id} removed from cart")

    def save(self):
        self.session.modified = True

    def __iter__(self):
        item_ids = self.cart.keys()
        items = Item.objects.filter(id__in=item_ids)

        for item in items:
            self.cart[str(item.id)]['item'] = item
        for item in self.cart.values():
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()


    def get_cart_items(self):
        item_ids = self.cart.keys()
        items = Item.objects.filter(id__in=item_ids)
        cart_items = []
        for item in items:
            cart_item = {
                'item': item,
                'quantity': self.cart[str(item.id)]['quantity']
            }
            cart_items.append(cart_item)
            #print(cart_item)
        return cart_items


    def update_quantity(self, item_id, quantity):
        item = Item.objects.get(id=item_id)
        self.cart[str(item.id)]['quantity'] = quantity
        self.save()
