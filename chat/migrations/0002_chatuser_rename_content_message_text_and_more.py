# Generated by Django 4.0.1 on 2023-04-20 18:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unread_messages', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unread_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='message',
            old_name='content',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='message',
            name='room',
        ),
        migrations.AddField(
            model_name='message',
            name='recipient',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='ChatRoom',
        ),
    ]
