# Generated by Django 3.1.3 on 2020-12-29 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('korbex', '0011_storeproducts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storeproducts',
            name='description',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='storeproducts',
            name='name_product',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
