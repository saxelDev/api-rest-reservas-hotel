from django.db import models

class Evento(models.Model):

    id_evento = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    capacidad_maxima = models.PositiveIntegerField()
    precio_entrada = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = "evento"
        ordering = ["id_evento"]
