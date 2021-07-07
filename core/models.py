from django.db import models
from django.db.models.base import Model
# Create your models here.

class Usuario(models.Model):
    idUsuario = models.IntegerField(primary_key=True, verbose_name="Id de usuario")
    email = models.CharField(max_length=50, blank=False, verbose_name="email del usuario")
    contraseña = models.CharField(max_length=12, blank=False, verbose_name="contraseña del usuario")
    tipoUsuario = models.CharField(max_length= 15, verbose_name="tipo de usuario")

    def __str__(self):
        return self.tipoUsuario

class Mecanico(models.Model):
    idMecanico = models.IntegerField(primary_key=True, verbose_name="id de Mecanico")
    nombreMecanico = models.CharField(max_length=60, verbose_name="nombre del mecanico")
    especialidad = models.CharField(max_length=30, verbose_name="especialidad del mecanico")
    fotoPerfil = models.CharField(max_length=100, verbose_name="foto del mecanico")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Trabajo(models.Model):
    idTrabajo = models.IntegerField(primary_key=True, verbose_name="id de Trabajo")
    nombreTrabajo = models.CharField(max_length=30, verbose_name="nombre de trabajo")
    foto = models.CharField(max_length=100, verbose_name="fotografia del trabajo")
    descripcion = models.CharField(max_length=250, verbose_name="descripcion del trabajo")
    categoria = models.CharField(max_length=30, verbose_name="categoria del trabajo")
    mecanico = models.ForeignKey(Mecanico, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreTrabajo

