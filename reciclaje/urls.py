from django.urls import path
from . import views

app_name = "reciclaje"
urlpatterns = [
    path("", views.index, name="index"),
    path("informacion/", views.informacion, name="informacion"),
    path("recoleccion/", views.recoleccion, name="recoleccion"),
]