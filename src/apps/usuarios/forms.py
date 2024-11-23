from .models import Usuario

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class UsuarioUpdateForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'avatar']
