from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    avatar = models.ImageField(upload_to='usuarios/', null=True, blank=True)