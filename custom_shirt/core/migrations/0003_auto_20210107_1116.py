# Generated by Django 3.1.4 on 2021-01-07 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210104_1812'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='discount_percent',
            new_name='discount_type',
        ),
    ]