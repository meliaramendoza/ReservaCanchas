from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class TipoCancha(models.Model):
    nombre_tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_tipo


class Ubicacion(models.Model):
    nombre_ubicacion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_ubicacion


class Cancha(models.Model):
    tipo_cancha = models.ForeignKey(TipoCancha, on_delete=models.CASCADE)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tipo_cancha} - {self.ubicacion}'


class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f'{self.usuario} - {self.cancha} - {self.fecha} - {self.hora}'
