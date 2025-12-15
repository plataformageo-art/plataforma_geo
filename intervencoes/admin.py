from django.contrib import admin
from .models import Intervencao, Comentario

@admin.register(Intervencao)
class IntervencaoAdmin(admin.ModelAdmin):
    list_display = ('categoria', 'usuario', 'data_registro')
    search_fields = ('categoria', 'descricao')
    list_filter = ('data_registro',)

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('texto', 'intervencao', 'usuario', 'data')
    search_fields = ('texto',)
    list_filter = ('data',)
