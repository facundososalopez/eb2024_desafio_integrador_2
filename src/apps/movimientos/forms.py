from django import forms
from .models import Movimiento

class MovimientoForm(forms.ModelForm):
    class Meta:
        model = Movimiento
        fields = ["tipo", "cuenta", "cuenta_asociada", "monto", "transferencia_motivo"]