from django.contrib import admin
from .models import Usuario, TipoCancha, Ubicacion, Cancha, Reserva

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo_electronico')
    ordering = ('correo_electronico',)
    search_fields = ('nombre', 'correo_electronico')

@admin.register(TipoCancha)
class TipoCanchaAdmin(admin.ModelAdmin):
    list_display = ('nombre_tipo',)
    ordering = ('nombre_tipo',)
    search_fields = ('nombre_tipo',)

@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    list_display = ('nombre_ubicacion',)
    ordering = ('nombre_ubicacion',)
    search_fields = ('nombre_ubicacion',)

@admin.register(Cancha)
class CanchaAdmin(admin.ModelAdmin):
    list_display = ('tipo_cancha', 'ubicacion')
    ordering = ('ubicacion', 'tipo_cancha')
    search_fields = ('tipo_cancha__nombre_tipo', 'ubicacion__nombre_ubicacion')  # Utilizamos la sintaxis "__" para buscar campos relacionados

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'cancha', 'fecha', 'hora')
    ordering = ('fecha', 'hora')
    search_fields = ('usuario__nombre', 'cancha__tipo_cancha__nombre_tipo', 'cancha__ubicacion__nombre_ubicacion')
