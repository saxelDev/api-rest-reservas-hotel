from django.db import models
from datetime import date

from bookings.models import Reserva

class Factura(models.Model):

    factura_id = models.AutoField(primary_key=True)
    reserva_id = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    fecha_emision = models.DateField(default=date.today)
    subtotal = models.DecimalField(max_digits=6, decimal_places=2)
    impuestos = models.DecimalField(max_digits=6, decimal_places=2)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    pagada = models.BooleanField(default=False)

    class Meta:
        db_table = 'factura'
        ordering = ["fecha_emision"]

