from django.db import models
from accounts.models import CustomUser, Deliveryman


class Order(models.Model):
    military = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders_military')
    items = models.TextField()
    date_order = models.DateTimeField(auto_now_add=True)
    delivery_location = models.CharField(max_length=200, blank=True, null=True)
    delivery_latitude = models.DecimalField(max_digits=15, decimal_places=12, blank=True, null=True)
    delivery_longitude = models.DecimalField(max_digits=15, decimal_places=12, blank=True, null=True)
    driver_latitude = models.DecimalField(max_digits=15, decimal_places=12, blank=True, null=True)
    driver_longitude = models.DecimalField(max_digits=15, decimal_places=12, blank=True, null=True)
    deliveryman = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='orders_deliveryman')
    volunteer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='orders_volunteer')
    date_arrival = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('delivered', 'Доставлено'), ('in_transit', 'В дорозі'), ('not_confirmed', 'Не підтверджено'), ('confirmed', 'Підтверджено'), ('is_expected','Очікується'), ('canceled','Скасовано')], default='')
    date_departure = models.DateField(null=True, blank=True)
    time_departure = models.TimeField(null=True, blank=True)

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'