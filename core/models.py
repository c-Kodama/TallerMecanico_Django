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

class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True, verbose_name="id categoria de trabajos")
    categoria = models.CharField(max_length=60, verbose_name="categoria de trabajos")

    def __str__(self):
        return self.categoria

class Mecanico(models.Model):
    idMecanico = models.IntegerField(primary_key=True, verbose_name="id de Mecanico")
    nombreMecanico = models.CharField(max_length=60, verbose_name="nombre del mecanico")
    especialidad = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fotoPerfil = models.CharField(max_length=100, verbose_name="foto del mecanico")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreMecanico



class Trabajo(models.Model):
    idTrabajo = models.IntegerField(primary_key=True, verbose_name="id de Trabajo")
    nombreTrabajo = models.CharField(max_length=30, verbose_name="nombre de trabajo")
    foto = models.CharField(max_length=100, verbose_name="fotografia del trabajo")
    descripcion = models.CharField(max_length=250, verbose_name="descripcion del trabajo")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    mecanico = models.ForeignKey(Mecanico, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreTrabajo

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    modelo_vehiculo = models.CharField(max_length=50)
    asunto = models.CharField()
    mensaje = models.TextField()
    
    def __str__(self):
        return self.asunto