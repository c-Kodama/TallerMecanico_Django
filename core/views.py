from django.shortcuts import render, redirect
from django.http import request

# Create your views here.

def Index(request):
    return render(request,'core/Index.html')

def galeria(request):
    return render(request, 'core/galeria.html')

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

    
