# Generated by Django 3.2 on 2022-11-04 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0013_auto_20221104_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, verbose_name='Nombres completos'),
        ),
    ]
