# Generated by Django 3.2.4 on 2021-07-13 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210713_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajo',
            name='fecha',
            field=models.DateField(),
        ),
    ]
