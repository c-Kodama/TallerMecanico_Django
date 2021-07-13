from django.db import models
from django.db.models.base import Model
# Create your models here.

class tipoUsuario(models.Model):
    id_tipoUsuario = models.IntegerField(primary_key=True, verbose_name="id tipo de usuario")
    tipoUsuario = models.CharField(max_length=60, verbose_name="tipos de usuario")
    
    def __str__(self):
        return self.tipoUsuario

class Usuario(models.Model):
    idUsuario = models.IntegerField(primary_key=True, verbose_name="Id de usuario")
    email = models.CharField(max_length=50, blank=False, verbose_name="email del usuario")
    contraseña = models.CharField(max_length=12, blank=False, verbose_name="contraseña del usuario")
    tipoUsuario = models.ForeignKey(tipoUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.email

class Mecanico(models.Model):
    idMecanico = models.IntegerField(primary_key=True, verbose_name="id de Mecanico")
    nombreMecanico = models.CharField(max_length=60, verbose_name="nombre del mecanico")
    especialidad = models.CharField(max_length=50, verbose_name="Especialidad del mecanico")
    fotoPerfil = models.CharField(max_length=100, verbose_name="foto del mecanico")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreMecanico

class Trabajo(models.Model):
    idTrabajo = models.IntegerField(primary_key=True, verbose_name="id de Trabajo")
    nombreTrabajo = models.CharField(max_length=30, verbose_name="nombre de trabajo")
    marca = models.CharField(max_length=30, default="marca", verbose_name="Marca del auto")
    modelo = models.CharField(max_length=30, default="modelo", verbose_name="Modelo del auto")
    fecha = models.DateField()
    categoria = models.CharField(max_length=50, verbose_name="Categoria del trabajo")
    descripcion = models.CharField(max_length=250, verbose_name="descripcion del trabajo")
    foto = models.CharField(max_length=100, verbose_name="fotografia del trabajo")
    mecanico = models.ForeignKey(Mecanico, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreTrabajo

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    modelo_vehiculo = models.CharField(max_length=50)
    asunto = models.CharField(max_length=60)
    mensaje = models.TextField()
    
    def __str__(self):
        return self.asunto