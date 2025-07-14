from django.db import models
from datetime import date

from users.models import Perfil
from hotel.models import Habitacion

class Reserva(models.Model):

    ESTADO = {
        "confirmada": "Confirmada",
        "cancelada": "Cancelada",
        "finalizada": "Finalizada"
    }

    reserva_id = models.AutoField(primary_key=True)
    cliente_id = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    habitacion_id = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    fecha_entrada = models.DateField(default=date.today, null=False)
    fecha_salida = models.DateField(null=False)
    estado = models.CharField(max_length=50, choices=ESTADO, default="confirmada")
    total_pagar = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        db_table = "reserva"
        ordering = ["reserva_id"]

