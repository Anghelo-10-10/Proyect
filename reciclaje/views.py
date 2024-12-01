from django.shortcuts import render, redirect
from django.template import loader
from .forms import PuntoAlmacenamientoForm

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    context = {
        'user': request.user,
        'logged_in': request.user.is_authenticated
    }
    return render(request, 'index.html', context)

def informacion(request):
    template = loader.get_template('informacion.html')
    return render(request, 'informacion.html')

def recoleccion(request):
    template = loader.get_template('recoleccion.html')
    return render(request, 'recoleccion.html')

def puntosrecoleccion(request):
    template = loader.get_template('puntosrecoleccion.html')
    return render(request, 'puntosrecoleccion.html')

def tiposderecoleccion(request):
    template = loader.get_template('tiposderecoleccion.html')
    return render(request, 'tiposderecoleccion.html')

def crear_punto_almacenamiento(request):
    if request.method == 'POST':
        form = PuntoAlmacenamientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('punto_recoleccion_form')
    else:
        form = PuntoAlmacenamientoForm()
    return render(request, 'punto_recoleccion_form.html', {'form': form})
