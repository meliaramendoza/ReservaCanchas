from django.contrib import admin
from .models import Usuario, TipoCancha, Ubicacion, Cancha, Reserva

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo_electronico')  # Columnas a mostrar en el listado
    ordering = ('correo_electronico',)  # Ordenar por correo electrónico

@admin.register(TipoCancha)
class TipoCanchaAdmin(admin.ModelAdmin):
    list_display = ('nombre_tipo',)
    ordering = ('nombre_tipo',)

@admin.register(Ubicacion)
class UbicacionAdmin(admin.ModelAdmin):
    list_display = ('nombre_ubicacion',)
    ordering = ('nombre_ubicacion',)

@admin.register(Cancha)
class CanchaAdmin(admin.ModelAdmin):
    list_display = ('tipo_cancha', 'ubicacion')
    ordering = ('ubicacion', 'tipo_cancha')  # Ordenar por ubicación y luego por tipo de cancha

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'cancha', 'fecha', 'hora')
    ordering = ('fecha', 'hora')  # Ordenar por fecha y luego por hora
