# Generated by Django 4.1.7 on 2023-04-18 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0016_order_date_arrival'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Замовлення', 'verbose_name_plural': 'Замовлення'},
        ),
    ]