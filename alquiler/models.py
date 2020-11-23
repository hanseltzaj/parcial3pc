from django.db import models
from django.contrib import admin
from django.utils import timezone

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateTimeField(blank=True, null=False)
    cliente = models.CharField(max_lenght=80)
    telefono = models.CharField(max_lenght=8)
    direccion = models.CharField(max_lenght=120)
    referencia = models.CharField(max_length=180)
    estado = models.CharField(max_length=10, blank=True, null=True)

    def atender(self):
        self.estado = "Atendido"
        self.save

    def __str__(self):
        return self.titulo

class Material(models.Model):
    
