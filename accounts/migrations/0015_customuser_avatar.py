# Generated by Django 4.1.7 on 2023-03-07 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_delete_customgroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='user_photo/%Y/%m/%d/'),
        ),
    ]
