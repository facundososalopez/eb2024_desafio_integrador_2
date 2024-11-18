# forms.py
from django import forms
from .models import MotivoTransferencia

class MotivoTransferenciaForm(forms.ModelForm):
    class Meta:
        model = MotivoTransferencia
        fields = ['descripcion']  # Incluye los campos del modelo que quieras mostrar

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Agrega la clase de Bootstrap al campo 'descripcion'
        self.fields['descripcion'].widget.attrs.update({
            'class': 'form-control',  # Clase de Bootstrap
            'placeholder': 'Escribe el motivo aquí...'  # Ejemplo de un atributo adicional
        })
