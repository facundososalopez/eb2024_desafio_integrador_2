from django.db import models
import os

from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    avatar = models.ImageField(upload_to='usuarios/', verbose_name='Avatar', null=True, blank=True)

    # _original_avatar se utiliza con signals para eliminar el archivo si se cambia o elimina
    __original_avatar = None