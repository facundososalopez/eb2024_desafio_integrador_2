from django.db import models

class MotivoTransferencia(models.Model):
    descripcion = models.CharField(max_length=100, verbose_name='Descripción')

    def __str__(self):
        return self.descripcion
        
    
