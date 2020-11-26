from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import EventoForm
from alquiler.models import Evento, Alquiler

def principal(request):
    return render(request, 'alquiler/principal.html')

def alquiler_nuevo(request):
    if request.method == "POST":
        formulario = EventoForm(request.POST)
        if formulario.is_valid():
            evento = Evento.objects.create(titulo=formulario.cleaned_data['titulo'], fecha=formulario.cleaned_data['fecha'], cliente=formulario.cleaned_data['cliente'], telefono=formulario.cleaned_data['telefono'], direccion=formulario.cleaned_data['direccion'], referencia=formulario.cleaned_data['referencia'])
            for material_id in request.POST.getlist('materials'):
                alquiler = Alquiler(material_id=material_id, evento_id=evento.id)
                alquiler.save()
            messages.add_message(request, messages.SUCCESS, 'Evento Guardado')
            formulario = EventoForm()
    else:
        formulario = EventoForm()
    return render(request, 'alquiler/alquiler_nuevo.html', {'formulario':formulario})

def alquiler_lista(request):
    eventos = Evento.objects.filter()
    return render(request, 'alquiler/alquiler_lista.html', {'eventos': eventos})

def alquiler_detalle(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    materiales = evento.materials.all()
    total = 0
    for material in materiales:
        total = total + material.costo
    return render(request, 'alquiler/alquiler_detalle.html', {'evento':evento, 'materiales':materiales, 'total':total})
