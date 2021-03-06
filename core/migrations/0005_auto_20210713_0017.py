# Generated by Django 3.2.4 on 2021-07-13 04:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210712_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajo',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='trabajo',
            name='marca',
            field=models.CharField(default='marca', max_length=30, verbose_name='Marca del auto'),
        ),
        migrations.AddField(
            model_name='trabajo',
            name='modelo',
            field=models.CharField(default='modelo', max_length=30, verbose_name='Modelo del auto'),
        ),
    ]
