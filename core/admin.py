from django.contrib import admin
from .models import Usuario, Mecanico, Trabajo, Categoria, tipoUsuario
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Mecanico)
admin.site.register(Trabajo)
admin.site.register(Categoria)
admin.site.register(tipoUsuario)