# Generated by Django 3.1.3 on 2021-01-30 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('korbex', '0022_auto_20210126_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homecontent',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='home_image'),
        ),
    ]
