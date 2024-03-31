from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin import ModelAdmin
from .models import CustomUser, Volunteer, Military, Deliveryman
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group



class RoleFilter(admin.SimpleListFilter):
    title = 'Role'
    parameter_name = 'role'

    def lookups(self, request, model_admin):
        return [
            ('volunteer', 'Volunteers'),
            ('military', 'Military'),
            ('deliveryman', 'Deliverymen')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'volunteer':
            return queryset.filter(volunteer__isnull=False)
        elif self.value() == 'military':
            return queryset.filter(military__isnull=False)
        elif self.value() == 'deliveryman':
            return queryset.filter(deliveryman__isnull=False)
        else:
            return queryset

class DeliveryStatusFilter(admin.SimpleListFilter):
    title = 'Status'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('IN_TRANSIT', 'В дорозі'),
            ('FREE', 'Вільний'),
            ('UNAVAILABLE', 'Недоступний'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'IN_TRANSIT':
            return queryset.filter(status='IN_TRANSIT')
        elif self.value() == 'FREE':
            return queryset.filter(status='FREE')
        elif self.value() == 'UNAVAILABLE':
            return queryset.filter(status='UNAVAILABLE')
        else:
            return queryset

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'get_role', 'first_name', 'last_name', 'email', 'phone', 'avatar', 'is_staff', 'is_active')
    list_filter = (RoleFilter,)
    readonly_fields = ('date_joined',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone', 'email', 'avatar')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    ordering = ('date_joined',)
    filter_horizontal = ('groups', 'user_permissions',)
    search_fields = ('username', 'first_name', 'last_name', 'email', 'phone')

    def get_role(self, obj):
        role = 'admin'
        if hasattr(obj, 'deliveryman'):
            return 'Deliveryman'
        elif hasattr(obj, 'volunteer'):
            return 'Volunteer'
        elif hasattr(obj, 'military'):
            return 'Military'
        elif obj.is_superuser == True:
            return 'admin'
        else:
            return '-'

    def save_model(self, request, obj, form, change):
        # Encrypt password if it's not already encrypted
        if not obj.password.startswith('pbkdf2_'):
            obj.password = make_password(obj.password)
        obj.save()

class UserAdminMixin:
    def user_username(self, obj):
        return obj.user.username
    
    def user_first_name(self, obj):
        return obj.user.first_name
    
    def user_last_name(self, obj):
        return obj.user.last_name
    
    def user_email(self, obj):
        return obj.user.email
    
    def user_phone(self, obj):
        return obj.user.phone

    def user_is_staff(self, obj):
        return obj.user.is_staff

    def user_is_active(self, obj):
        return obj.user.is_active

class MilitaryAdmin(UserAdminMixin, admin.ModelAdmin):
    #model = Military
    list_display = ('user_username', 'military_unit', 'military_rank','user_first_name', 'user_last_name', 'user_email', 'user_phone', 'user_is_staff', 'user_is_active',  )
    search_fields = ('user__username', 'military_unit', 'user__first_name', 'user__last_name', 'user__email', 'user__phone')

class VolunteerAdmin(UserAdminMixin, admin.ModelAdmin):
    #model = Volunteer
    list_display = ('user_username', 'user_first_name', 'user_last_name', 'user_email', 'user_phone', 'user_is_staff', 'user_is_active',)
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'user__email', 'user__phone')

class DeliverymanAdmin(UserAdminMixin, admin.ModelAdmin):
    #model = Deliveryman
    list_display = ('user_username', 'status','user_first_name', 'user_last_name', 'user_email', 'user_phone', 'user_is_staff', 'user_is_active')
    search_fields = ('user__username', 'status', 'user__first_name', 'user__last_name', 'user__email', 'user__phone')
    list_filter = (DeliveryStatusFilter,)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Deliveryman, DeliverymanAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Military, MilitaryAdmin)





# logentry
# volunteer
# military
# deliveryman
# id
# password
# last_login
# is_superuser
# username
# first_name
# last_name
# info
# email
# phone
# date_joined
# is_staff
# is_active
# groups
# user_permissions

# fields = CustomUser._meta.get_fields()
# #print(fields)
# for field in fields:
#     print(field.name)