from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    """
    Modelo que representa un cliente del hotel
    """
    ROLES = {
        "admin": "Administrador",
        "recepcionista": "Recepcionista",
        "cliente": "Cliente",
    }
    perfil_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dni = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    rol = models.CharField(max_length=20, choices=ROLES, default=ROLES["cliente"])

    class Meta:
        #nombre de la tabla en la base de datos
        db_table = "perfil"
        #orden de los registros por defecto
        ordering = ["perfil_id"]
