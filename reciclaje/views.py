from django.shortcuts import render
from django.template import loader

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