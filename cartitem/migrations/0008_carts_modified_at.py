# Generated by Django 4.1.7 on 2023-04-05 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartitem', '0007_alter_carts_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='carts',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]