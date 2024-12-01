from django.urls import path
from . import views

app_name = "reciclaje"
urlpatterns = [
    path("", views.index, name="index"),
    path("informacion/", views.informacion, name="informacion"),
    path("recoleccion/", views.recoleccion, name="recoleccion"),
    path("reciclaje/puntosrecoleccion/", views.puntosrecoleccion, name="puntosrecoleccion"),
    path("reciclaje/tiposderecoleccion/", views.tiposderecoleccion, name="tiposderecoleccion"),
]