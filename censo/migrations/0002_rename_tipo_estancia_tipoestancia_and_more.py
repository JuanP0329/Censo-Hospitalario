# Generated by Django 4.2.3 on 2023-07-14 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('censo', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tipo_estancia',
            new_name='TipoEstancia',
        ),
        migrations.AlterModelOptions(
            name='tipoestancia',
            options={'verbose_name': 'Tipo estancia', 'verbose_name_plural': 'Tipo estancias'},
        ),
    ]
