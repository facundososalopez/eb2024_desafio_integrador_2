from django import forms
from .models import Movimiento
from apps.transferencia_motivo.models import MotivoTransferencia
from apps.usuarios.models import Usuario

class MovimientoForm(forms.ModelForm):
    class Meta:
        model = Movimiento
        fields = ["tipo", "cuenta", "cuenta_asociada", "monto", "transferencia_motivo"]


class TransferenciaForm(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Extrae el usuario de los kwargs
        super().__init__(*args, **kwargs)

        # Filtra el queryset de 'cuenta_asociada_id' para excluir al usuario actual
        if user:
            self.fields['cuenta_asociada_id'].queryset = Usuario.objects.exclude(id=user.id)
    cuenta_asociada_id = forms.ModelChoiceField(
        queryset=Usuario.objects.all(),
        label="Selecciona la cuenta destino:",
        required=True,
    )
    monto = forms.DecimalField(
        label="Monto:",
        max_digits=10,
        decimal_places=2,
        min_value=10,
        required=True
    )
    transferencia_motivo = forms.ModelChoiceField(
        queryset=MotivoTransferencia.objects.all(),
        required=True,
        label="Selecciona el motivo de la transferencia:"
    )
def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # Obtiene el usuario de los argumentos
        super().__init__(*args, **kwargs)
        if user:
            self.fields['cuenta_asociada_id'].queryset = Usuario.objects.exclude(id=user.id)

class IngresoDineroForm(forms.Form):
    monto = forms.DecimalField(
        label="Monto a ingresar:",
        max_digits=10,
        decimal_places=2,
        min_value=0.01,
        required=True,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "Ingrese el monto"})
    ) # Excluye al usuario logueado