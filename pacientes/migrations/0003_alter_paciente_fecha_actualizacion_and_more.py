# Generated by Django 4.2.3 on 2023-07-13 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0002_delete_auditoria_paciente_fecha_actualizacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='fecha_actualizacion',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
