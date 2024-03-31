from django.contrib.auth.models import Permission

volunteer_permissions = [
    Permission.objects.get(codename='add_category'),
    Permission.objects.get(codename='change_category'),
    Permission.objects.get(codename='delete_category'),

    Permission.objects.get(codename='add_subcategory'),
    Permission.objects.get(codename='change_subcategory'),
    Permission.objects.get(codename='delete_subcategory'),

    Permission.objects.get(codename='add_item'),
    Permission.objects.get(codename='change_item'),
    Permission.objects.get(codename='delete_item'),

    Permission.objects.get(codename='view_military'),
    Permission.objects.get(codename='view_volunteer'),
    Permission.objects.get(codename='view_deliveryman'),
]