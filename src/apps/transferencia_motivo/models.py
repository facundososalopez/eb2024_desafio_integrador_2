from django.db import models

class MotivoTransferencia(models.Model):
    descripcion = models.CharField(max_length=100, unique=True, verbose_name='Descripción')
    
    #agregar clase de boostrap form-text

    def __str__(self):
        return self.descripcion
        
    
