# Generated by Django 4.1.7 on 2023-03-10 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='user_photo/%Y/%m/%d/'),
        ),
    ]
