from django.shortcuts import render, redirect
from .models import Juego
from .forms import JuegoForm

# Create your views here.
def home(request):
    juegos = Juego.objects.all()
    datos = {
        'juegos': juegos
    }
    return render(request, 'core/home.html', datos)

def agregar_juego(request):
    datos = {
        'form': JuegoForm() 
        }
    if request.method == 'POST':
        formulario_add = JuegoForm(request.POST)
        if formulario_add.is_valid:
            formulario_add.save()
            datos['mensaje'] = "Juego Agregado Correctamente"
    return render(request, 'core/agregar_juego.html', datos)

def editar_juego(request, pk):
    juego = Juego.objects.get(pegi=pk)
    datos = {
        'form': JuegoForm(instance=juego) 
        }
    if request.method == 'POST':
        formulario_edit = JuegoForm(data=request.POST, instance=juego)
        if formulario_edit.is_valid:
            formulario_edit.save()
            datos['mensaje'] = "Juego Editado Correctamente"
    return render(request, 'core/editar_juego.html', datos)

def borrar_juego(request, pk):
    juegos = Juego.objects.get(pegi=pk)
    juegos.delete()
    return redirect(to="home")

def blog(request):
    return render(request, 'core/blog.html')