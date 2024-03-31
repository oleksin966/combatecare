# Generated by Django 4.1.7 on 2023-04-18 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0002_item_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категорія', 'verbose_name_plural': 'Категорії'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Предмет', 'verbose_name_plural': 'Предмети'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': 'Підкатегорія', 'verbose_name_plural': 'Підкатегорії'},
        ),
    ]