from django.contrib import admin
from .models import Usuario, Mecanico, Trabajo, tipoUsuario, Contacto
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Mecanico)
admin.site.register(Trabajo)
admin.site.register(tipoUsuario)
admin.site.register(Contacto)