# Generated by Django 3.1.4 on 2021-01-22 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210122_1352'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItemCategoryAppend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
