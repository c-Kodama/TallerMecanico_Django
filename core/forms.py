from django import forms
from .models import Contacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = ("nombre", "correo", "modelo_vehiculo", "asunto", "mensaje")


class CustomCreationForm(UserCreationForm):

    class Meta:
        model = User
        field= ("username", "first_name", "last_name", "email", "password1", "password2")

