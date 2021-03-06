# Generated by Django 3.2.4 on 2021-07-08 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='id categoria de trabajos')),
                ('categoria', models.CharField(max_length=60, verbose_name='categoria de trabajos')),
            ],
        ),
        migrations.CreateModel(
            name='tipoUsuario',
            fields=[
                ('id_tipoUsuario', models.IntegerField(primary_key=True, serialize=False, verbose_name='id tipo de usuario')),
                ('tipoUsuario', models.CharField(max_length=60, verbose_name='tipos de usuario')),
            ],
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='tipoUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipousuario'),
        ),
    ]
