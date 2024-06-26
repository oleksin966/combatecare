# Generated by Django 4.1.7 on 2023-04-05 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('warehouse', '0002_item_slug'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cartitem', '0003_remove_cartitem_cart_remove_cartitem_item_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('session_key', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'verbose_name': 'Кошик',
                'verbose_name_plural': 'Кошики',
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cartitem.cart')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.item')),
            ],
            options={
                'verbose_name': 'Предмет в кошику',
                'verbose_name_plural': 'Предмети в кошику',
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(through='cartitem.CartItem', to='warehouse.item'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
