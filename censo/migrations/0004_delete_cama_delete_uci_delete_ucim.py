# Generated by Django 4.2.3 on 2023-07-17 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('censo', '0003_tipoestancia_capacidad'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cama',
        ),
        migrations.DeleteModel(
            name='Uci',
        ),
        migrations.DeleteModel(
            name='Ucim',
        ),
    ]
