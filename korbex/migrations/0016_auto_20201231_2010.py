# Generated by Django 3.1.3 on 2020-12-31 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('korbex', '0015_storeproducts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addres', models.TextField(blank=True, max_length=200)),
                ('telefon', models.TextField(blank=True, max_length=200)),
                ('facebok', models.URLField(blank=True, verbose_name='facebook')),
            ],
        ),
        migrations.CreateModel(
            name='WorkingHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('working_day', models.CharField(max_length=20)),
                ('working_hours', models.CharField(max_length=25)),
            ],
        ),
        migrations.AlterField(
            model_name='storeproducts',
            name='continue_description',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='storeproducts',
            name='incomplete_description',
            field=models.TextField(max_length=130),
        ),
    ]
