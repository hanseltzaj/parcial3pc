from django.contrib import admin
from alquiler.models import Evento, EventoAdmin, Material, MaterialAdmin

admin.site.register(Evento, EventoAdmin)
admin.site.register(Material, MaterialAdmin)
