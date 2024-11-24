from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models import Count
from apps.transferencia_motivo.models import MotivoTransferencia
import django_filters
from django.forms import TextInput, Select, DateInput

class MovimientoManager(models.Manager):
    def cuentas_mas_utilizadas(self, usuario, limite=10):
        return (
            self.get_queryset()
            .filter(cuenta=usuario)  # Filtra por el usuario logueado
            .values('cuenta_asociada', 'cuenta_asociada__username')  # Agrupa por la cuenta asociada
            .annotate(total=Count('cuenta_asociada'))  # Cuenta la cantidad de movimientos por cuenta asociada
            .order_by('-total')[:limite] # Ordenar por cantidad de uso
        )
class Movimiento(models.Model):
    TIPO_CHOICES = [
        (1, "Ingreso de dinero"),
        (2, "Transferencia enviada"),
        (3, "Transferencia recibida"),
    ]

    tipo = models.PositiveSmallIntegerField(choices=TIPO_CHOICES)
    cuenta = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="movimientos")
    cuenta_asociada = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="movimientos_asociados"
    )
    transferencia_motivo = models.ForeignKey("transferencia_motivo.MotivoTransferencia", on_delete=models.SET_NULL, null=True, blank=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    objects = MovimientoManager()

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.monto} ({self.fecha})"
    
    def save(self, *args, **kwargs):
        # Modificar un parámetro antes de guardar
         if self.tipo == 2:
            self.cuenta =  self.cuenta * -1
         if self.tipo == 4:
            self.monto =  self.monto * -1
         super().save(*args, **kwargs)

class MovimientoFilter(django_filters.FilterSet):
    fecha = django_filters.DateFromToRangeFilter(
        field_name='fecha',
        label="Rango de Fechas",
        widget=django_filters.widgets.RangeWidget(  # Define RangeWidget aquí
            attrs={
                'class': 'form-control form-control-sm', 
                'type': 'date'  # Selector de fechas HTML5
            }
        )
    )
    cuenta_asociada = django_filters.CharFilter(
        field_name='cuenta_asociada__username',
        lookup_expr='icontains',
        label="Cuenta Asociada",
        widget=TextInput(attrs={'class': 'form-control form-control-sm'})
    )
    tipo = django_filters.ChoiceFilter(
        choices=Movimiento.TIPO_CHOICES,
        label="Tipo",
        widget=Select(attrs={'class': 'form-select form-select-sm'})
    )
    monto = django_filters.RangeFilter(
        field_name='monto',
        label="Rango de Monto",
        widget=django_filters.widgets.RangeWidget(
            attrs={'class': 'form-control form-control-sm', 'placeholder': 'Monto'}
        )
    )
    transferencia_motivo = django_filters.ModelChoiceFilter(
        queryset=MotivoTransferencia.objects.all(),  # Opciones dinámicas desde el modelo relacionado
        label="Motivo de Transferencia",
        widget=Select(attrs={'class': 'form-select form-select-sm'})
    )

    class Meta:
        model = Movimiento
        fields = ['fecha', 'cuenta_asociada', 'tipo', 'monto', 'transferencia_motivo']

#models y filters para admin
class MovimientoAdmin(models.Model):
    TIPO_CHOICES = [
        (1, "Ingreso de dinero"),
        (2, "Transferencia enviada"),
        (3, "Transferencia recibida"),
    ]

    tipo = models.PositiveSmallIntegerField(choices=TIPO_CHOICES)
    cuenta = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="admin_movimientos")
    cuenta_asociada = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="admin_movimientos_asociados"
    )
    transferencia_motivo = models.ForeignKey("transferencia_motivo.MotivoTransferencia", on_delete=models.SET_NULL, null=True, blank=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.monto} ({self.fecha})"

class MovimientoAdminFilter(django_filters.FilterSet):
    fecha = django_filters.DateFromToRangeFilter(
        field_name='fecha',
        label="Rango de Fechas",
        widget=django_filters.widgets.RangeWidget(  # Define RangeWidget aquí
            attrs={
                'class': 'form-control form-control-sm', 
                'type': 'date'  # Selector de fechas HTML5
            }
        )
    )

    cuenta = django_filters.CharFilter(
        field_name='cuenta__username',
        lookup_expr='icontains',
        label="Cuenta Origen",
        widget=TextInput(attrs={'class': 'form-control form-control-sm'})
    )

    cuenta_asociada = django_filters.CharFilter(
        field_name='cuenta_asociada__username',
        lookup_expr='icontains',
        label="Cuenta Destino",
        widget=TextInput(attrs={'class': 'form-control form-control-sm'})
    )
     
    tipo = django_filters.ChoiceFilter(
        choices=MovimientoAdmin.TIPO_CHOICES,
        label="Tipo",
        widget=Select(attrs={'class': 'form-select form-select-sm'})
    )
    monto = django_filters.RangeFilter(
        field_name='monto',
        label="Rango de Monto",
        widget=django_filters.widgets.RangeWidget(
            attrs={'class': 'form-control form-control-sm', 'placeholder': 'Monto'}
        )
    )
    transferencia_motivo = django_filters.ModelChoiceFilter(
        queryset=MotivoTransferencia.objects.all(),  # Opciones dinámicas desde el modelo relacionado
        label="Motivo de Transferencia",
        widget=Select(attrs={'class': 'form-select form-select-sm'})
    )

    class Meta:
        model = MovimientoAdmin
        fields = ['fecha',  'cuenta', 'cuenta_asociada', 'tipo', 'monto', 'transferencia_motivo']

    
