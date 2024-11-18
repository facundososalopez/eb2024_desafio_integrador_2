from django.contrib import admin
from .models import MotivoTransferencia

@admin.register(MotivoTransferencia)
class MotivoTransferenciaAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripcion')
    search_fields = ('descripcion',)

# Register your models here.
