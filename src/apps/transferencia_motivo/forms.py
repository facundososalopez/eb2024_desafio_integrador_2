# forms.py
from django import forms
from .models import MotivoTransferencia

class MotivoTransferenciaForm(forms.ModelForm):
    class Meta:
        model = MotivoTransferencia
        fields = ['descripcion']  # Incluye los campos del modelo que quieras mostrar


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Agrega la un place holder al input
        self.fields['descripcion'].widget.attrs.update({
            'placeholder': 'Escribe el motivo aquí...'  # Ejemplo de un atributo adicional
        })
