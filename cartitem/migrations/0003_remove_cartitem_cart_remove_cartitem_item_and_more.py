# Generated by Django 4.1.7 on 2023-03-13 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cartitem', '0002_cart_session_key_alter_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='item',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
