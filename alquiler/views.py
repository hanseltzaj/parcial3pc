from django.shortcuts import render
from django.contrib import messages
from .forms import EventoForm
from alquiler.models import Evento, Alquiler

def alquiler_nuevo(request):
    if request.method == "POST":
        formulario = EventoForm(request.POST)
        if formulario.is_valid():
            evento = Evento.objects.create(titulo=formulario.cleaned_data['titulo'], fecha=formulario.cleaned_data['fecha'], cliente=formulario.cleaned_data['cliente'], telefono=formulario.cleaned_data['telefono'], direccion=formulario.cleaned_data['direccion'], referencia=formulario.cleaned_data['referencia'])
            for material_id in request.POST.getlist('materials'):
                alquiler = Alquiler(material_id=material_id, evento_id=evento.id)
                alquiler.save()
            messages.add_message(request, messages.SUCCESS, 'Evento Guardado')
    else:
        formulario = EventoForm()

    return render(request, 'alquiler/alquiler_nuevo.html', {'formulario':formulario})
