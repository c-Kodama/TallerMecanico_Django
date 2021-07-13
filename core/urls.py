from django.urls import path
from .views import Index, galeria, profesionales, contacto, login, MecanicoIndex, MecanicoTrabajos, PublicarTrabajo, registro, modificarTrabajo


urlpatterns = [
    path('', Index, name="Index"),
    path('galeria/', galeria, name="galeria"),
    path('profesionales', profesionales, name="profesionales"),
    path('contacto', contacto, name="contacto"),
    path('login', login, name="login"),
    path('MecanicoIndex', MecanicoIndex, name="MecanicoIndex"),
    path('MecanicoTrabajos', MecanicoTrabajos, name="MecanicoTrabajos"),
    path('PublicarTrabajo', PublicarTrabajo, name="PublicarTrabajo"),
    path('registro', registro, name="registro"),
    path('modificarTrabajo', modificarTrabajo, name="modificarTrabajo")
    
]