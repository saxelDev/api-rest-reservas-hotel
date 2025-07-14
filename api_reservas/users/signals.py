from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Perfil

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Señal para crear un perfil cuando se crea un nuevo usuario.
    """
    if created:
        Perfil.objects.create(user=instance)
