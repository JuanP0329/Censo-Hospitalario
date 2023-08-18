# Generated by Django 4.2.3 on 2023-08-17 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comorbidity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Comorbidity',
                'verbose_name_plural': 'Comorbidities',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='medicalhistory',
            name='condition',
            field=models.CharField(blank=True, choices=[('dead', 'Dead'), ('live', 'Live'), ('review', 'Under Review')], max_length=20, null=True),
        ),
    ]