from django.db import models

# Create your models here.

class Reserva(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    email = models.EmailField(default='')
    servicio = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()
    fecha_hora = models.DateTimeField()
    

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.creditos)
