# Generated by Django 4.1.7 on 2023-03-27 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ordering', '0009_remove_order_date_arrival'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_arrival', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('В дорозі', 'В дорозі'), ('Доставлено', 'Доставлено')], default='-', max_length=20)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_order', to='ordering.order')),
            ],
        ),
    ]
