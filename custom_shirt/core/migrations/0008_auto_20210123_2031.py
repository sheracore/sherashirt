# Generated by Django 3.1.4 on 2021-01-23 20:31

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210123_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='/vol/web/media/uploads/product/43475daa-f7d0-45d7-819f-c3e18b2afedc.jpg', null=True, upload_to=core.models.product_image_file_path),
        ),
    ]
