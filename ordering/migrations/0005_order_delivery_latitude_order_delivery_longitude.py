# Generated by Django 4.1.7 on 2023-03-24 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0004_order_date_departure_order_time_departure'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]
