from django.db import models
from django.contrib import admin
from django.utils import timezone

class Material(models.Model):
    nombre = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits = 8, decimal_places = 2)

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateTimeField(blank=True, null=False)
    cliente = models.CharField(max_length=80)
    telefono = models.CharField(max_length=8)
    direccion = models.CharField(max_length=120)
    referencia = models.CharField(max_length=180)
    estado = models.CharField(max_length=10, blank=True, null=True)
    materials = models.ManyToManyField(Material, through='Alquiler')

    def atender(self):
        self.estado = "Atendido"
        self.save

    def __str__(self):
        return self.titulo

class Alquiler(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)

class AlquilerInLine(admin.TabularInline):
    model = Alquiler
    extra = 1

class EventoAdmin(admin.ModelAdmin):
    inlines = (AlquilerInLine,)

class MaterialAdmin(admin.ModelAdmin):
    inlines = (AlquilerInLine,)
