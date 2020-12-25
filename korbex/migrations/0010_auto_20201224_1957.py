# Generated by Django 3.1.3 on 2020-12-24 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('korbex', '0009_auto_20201224_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeRepair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_repair', models.CharField(help_text='Typ naprawy(kierownica, hamulca itp)', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='service',
            name='type_repair',
            field=models.ForeignKey(default='other', on_delete=django.db.models.deletion.SET_DEFAULT, to='korbex.typerepair'),
        ),
    ]
