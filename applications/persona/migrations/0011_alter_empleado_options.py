# Generated by Django 3.2 on 2022-11-03 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0010_empleado_full_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['first_name', 'last_name'], 'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados de la empresa'},
        ),
    ]
