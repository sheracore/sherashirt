# Generated by Django 3.1.4 on 2021-01-08 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210108_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='weight_gram',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
