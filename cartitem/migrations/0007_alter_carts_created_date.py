# Generated by Django 4.1.7 on 2023-04-05 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartitem', '0006_rename_cart_carts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carts',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
