# Generated by Django 3.1.4 on 2021-01-22 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210122_1555'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitemappendcategory',
            old_name='name',
            new_name='type_name',
        ),
    ]
