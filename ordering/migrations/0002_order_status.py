# Generated by Django 4.1.7 on 2023-03-21 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Доставлено', 'Доставлено'), ('В дорозі', 'В дорозі'), ('Не підтверджено', 'Не підтверджено'), ('Підтверджено', 'Підтверджено')], default='Не підтверджено', max_length=20),
        ),
    ]
