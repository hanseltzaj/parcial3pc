from django import forms
from .models import Evento, Material

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ('titulo', 'fecha', 'cliente', 'telefono', 'direccion', 'referencia', 'materials')

    def __init__ (self, *args, **kwargs):
        super(EventoForm, self).__init__(*args, **kwargs)
        self.fields["materials"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["materials"].help_text = "Seleccione materiales a utilizar en el evento"
        self.fields["materials"].queryset = Material.objects.all()
