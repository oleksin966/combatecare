# Generated by Django 4.1.7 on 2023-03-10 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_alter_userprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, default='/static/account/img/noavatar.png', null=True, upload_to='update_user_photo/%Y/%m/%d/'),
        ),
    ]
