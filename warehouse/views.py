from django.shortcuts import render, get_object_or_404
from .models import Item, Category, Subcategory
from django.db.models import Q
from cartitem.cart import Cart
from cartitem.views import remove_from_cart


def item_list(request):
    items = Item.objects.all()

    selected_category = request.GET.get('category', None)
    if selected_category:
        items = items.filter(category=selected_category)

    selected_subcategory = request.GET.get('subcategory', None)
    if selected_subcategory:
        items = items.filter(subcategory=selected_subcategory)

    search_term = request.GET.get('search', None)
    if search_term:
        items = items.filter(Q(name__icontains=search_term) | Q(description__icontains=search_term))

    categories = Category.objects.all()

    if selected_category:
        subcategories = Subcategory.objects.filter(category=selected_category)
    else:
        subcategories = None

    cart = Cart(request)
    cart_items = cart.get_cart_items()
    #print(cart_items)

    context = {
        'items': items,
        'cart': cart,
        'cart_items': cart_items,
        'categories': categories,
        'subcategories': subcategories,
        'selected_category': int(selected_category) if selected_category else None,
        'selected_subcategory': int(selected_subcategory) if selected_subcategory else None,
    }

    return render(request, 'list_item.html', context)


def item_detail(request, slug):
    item = get_object_or_404(Item, slug=slug)
    return render(request, 'item_detail.html', {'item': item})