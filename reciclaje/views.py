from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from .forms import PuntoAlmacenamientoForm
from django.http import HttpResponse
from .models import PuntoAlmacenamiento

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
            return redirect('reciclaje:puntosrecoleccion')
    else:
        form = PuntoAlmacenamientoForm()
    return render(request, 'punto_recoleccion_form.html', {'form': form})

def puntorecoleccion(request, puntorecoleccion_id):
    punto = get_object_or_404(PuntoAlmacenamiento, pk = puntorecoleccion_id)
    template = loader.get_template('display_puntosrecoleccion.html')
    context = {
        'punto': punto
    }
    return HttpResponse(template.render(context, request))


def puntosrecoleccion(request):
    puntos = PuntoAlmacenamiento.objects.order_by('nombre')
    template = loader.get_template('puntosrecoleccion.html')
    context = {
        'puntos': puntos
    }
    return HttpResponse(template.render(context, request))


def edit_puntosrecoleccion(request):
    if request.method == 'POST':
        form = PuntoAlmacenamientoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('reciclaje:puntosrecoleccion')
    else:
        form = PuntoAlmacenamientoForm()
    
    return render(request, 'punto_recoleccion_form.html', {'form': form})


def delete_puntosrecoleccion(request, id):
    puntosrecoleccion = get_object_or_404(PuntoAlmacenamiento, pk = id)
    puntosrecoleccion.delete()
    return redirect("reciclaje:puntosrecoleccion") 

