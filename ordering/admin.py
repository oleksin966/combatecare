from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('military', 'date_order', 'status')
    list_filter = ('status',)
    search_fields = ('military__username', 'items')

admin.site.register(Order, OrderAdmin)
