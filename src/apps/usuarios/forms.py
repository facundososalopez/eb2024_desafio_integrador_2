from .models import Usuario

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class UsuarioUpdateForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['email', 'first_name', 'last_name', 'avatar']

class AdminUsuarioUpdateForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['is_active', 'email', 'first_name', 'last_name', 'avatar', 'is_staff']

