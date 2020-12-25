# Generated by Django 3.1.3 on 2020-12-23 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('korbex', '0005_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_repair', models.CharField(help_text='Nazwa naprawy(wymiana kierownicy)', max_length=30)),
                ('type_repair', models.CharField(help_text='Typ naprawy(kierownica, hamulca itp)', max_length=50, unique=True)),
                ('cena', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(help_text='Imie awtora tekstu', max_length=20),
        ),
    ]