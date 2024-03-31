from django.contrib import admin
from .models import Category, Subcategory, Item


class CategoryListFilter(admin.SimpleListFilter):
    title = 'Category'
    parameter_name = 'category'

    def lookups(self, request, model_admin):
        categories = Category.objects.all()
        return [(c.id, c.name) for c in categories]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(category__id=self.value())

class SubcategoryListFilter(admin.SimpleListFilter):
    title = 'Subcategory'
    parameter_name = 'subcategory'

    def lookups(self, request, model_admin):
        subcategories = Subcategory.objects.all()
        return [(s.id, s.name) for s in subcategories]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(subcategory__id=self.value())

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'subcategory', 'quantity', 'description', 'photo',)
    list_editable = ['quantity',]
    list_filter = [CategoryListFilter, SubcategoryListFilter]
    fields = ('name', 'slug', 'category', 'subcategory', 'quantity', 'description', 'photo',)
    search_fields = ['name', 'description']  # Add search fields here


admin.site.register(Item, ItemAdmin)
admin.site.register(Category)
admin.site.register(Subcategory)


