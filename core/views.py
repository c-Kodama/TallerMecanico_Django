from django.shortcuts import render, redirect
from django.http import request
from .models import Mecanico, Trabajo

# Create your views here.

def Index(request):
    mecanicos = Mecanico.objects.all()
    trabajos = Trabajo.objects.all()
    datos = {
        'listaMecanicos': mecanicos,
        'listaTrabajos': trabajos
        }
    return render(request,'core/Index.html', datos)

def galeria(request):
    trabajos = Trabajo.objects.all()
    datos = {
        'listaTrabajos': trabajos
    }
    return render(request, 'core/galeria.html', datos)

def profesionales(request):
    return render(request, 'core/profesionales.html')

def contacto(request):
    return render(request, 'core/formulariocontacto.html')

def login(request):
    return render(request, 'core/Registro-login.html')

def MecanicoIndex(request):
    return render(request, 'core/Mecanic.html')

def MecanicoTrabajos(request):
    return render(request, 'core/mecanicTrabajos.html')

def PublicarTrabajo(request):
    return render(request, 'core/form_publicar')

    
