# Generated by Django 3.1.4 on 2021-02-19 16:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='create_order_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
