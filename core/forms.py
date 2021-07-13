from django import forms
from .models import Contacto, Trabajo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

    
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ("nombre", "correo", "modelo_vehiculo", "asunto", "mensaje")


class CustomCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

class publicarForm(forms.ModelForm):
    class Meta:
        model = Trabajo
        fields = ['idTrabajo', 'nombreTrabajo', 'marca', 'modelo', 'fecha', 'categoria', 'descripcion', 'mecanico', 'foto']

