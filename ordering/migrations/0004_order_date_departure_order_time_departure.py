# Generated by Django 4.1.7 on 2023-03-24 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0003_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_departure',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='time_departure',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
