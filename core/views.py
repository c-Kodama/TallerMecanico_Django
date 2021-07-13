from django.shortcuts import render, redirect
from django.http import request
from .models import Mecanico, Trabajo
from .forms import ContactoForm, CustomCreationForm, publicarForm
from django.contrib.auth import authenticate, login
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

#def contacto(request):
    #return render(request, 'core/formulariocontacto.html')

def contacto(request):
    data = {
        'form': ContactoForm()

    }
    if request.method == 'POST':
        formulario=ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto guardado"
        else:
            data["form"] = formulario

    return render(request, 'core/formulariocontacto.html', data)

def login(request):
    return render(request, 'core/Registro-login.html')

def MecanicoIndex(request):
    return render(request, 'core/Mecanic.html')

def MecanicoTrabajos(request):
    return render(request, 'core/mecanicTrabajos.html')

def PublicarTrabajo(request):
    datos = { 
        'form': publicarForm() 
        }
    if request.method == 'POST':
        formulario = publicarForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "¡Publicado!"   
        else:
            datos['form'] = formulario 
    return render(request, 'core/form_publicar.html', datos)

def modificarTrabajo(request):
    trabajo = Trabajo.objects.get(nombreTrabajo=id)
    datos = {
        'form': publicarForm(instance=trabajo)
    }
    if request.method == 'POST':
        formulario = publicarForm(data=request.POST, instance=trabajo)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Editado correctamente"
    return render(request, 'core/mod_publicacion.html')
    
def registro(request):
    data={
        'form': CustomCreationForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formluario.cleaned_data["password1"])
            login(request, user)
            messages.succes(request,"Te haz registrado correctamente")
            #redirigir al index
            return redirect(to="Index")
        data["form"] = formulario

    return render(request,'registration/registro.html', data)