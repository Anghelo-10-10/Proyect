from django.db import models

# Create your models here.

class PuntoAlmacenamiento(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.TextField()
    ciudad = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    horario_apertura = models.CharField(max_length=100, blank=True, null=True)
    capacidad_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.nombre