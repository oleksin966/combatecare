# Generated by Django 4.1.7 on 2023-03-07 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_customgroup'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomGroup',
        ),
    ]