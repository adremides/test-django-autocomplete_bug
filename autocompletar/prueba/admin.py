from django.contrib import admin
from .models import *

class ConceptoAdmin(admin.ModelAdmin):
    model = Concepto
    ordering = ['descripcion']
    search_fields = ['descripcion']

class MovimientoAdmin(admin.ModelAdmin):
    model = Movimiento
    autocomplete_fields = ('concepto',)

class Bug_MovimientoAdmin(admin.ModelAdmin):
    model = Movimiento
    autocomplete_fields = ('concepto',)

admin.site.register(Concepto, ConceptoAdmin)
admin.site.register(Movimiento, MovimientoAdmin)
admin.site.register(Bug_Movimiento, Bug_MovimientoAdmin)