from django.db import models

class Habitacion(models.Model):
    """
    Modelo que representa un hotel.
    """
    TIPOS = {
        "INDIVIDUAL": "individual",
        "DOBLE": "doble",
        "SUITE": "suite"
    }
    habitacion_id = models.AutoField(primary_key=True)
    numero = models.IntegerField()
    tipo = models.CharField(max_length=50, choices=TIPOS, default=TIPOS["INDIVIDUAL"])
    precio_noche = models.DecimalField(max_digits=6, decimal_places=2)
    disponible = models.BooleanField(default=True)

    class Meta:
        #nombre de la tabla en la base de datos
        db_table = "habitacion"
        #orden de los registros por defecto
        ordering = ['habitacion_id']

