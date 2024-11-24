from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect
from .forms import UsuarioForm, UsuarioUpdateForm, AdminUsuarioUpdateForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.decorators import login_not_required
from django.utils.decorators import method_decorator
from apps.movimientos.models import Movimiento
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

from django_filters.views import FilterView

from .models import Usuario

# Create your views here.

@method_decorator(login_not_required, name='dispatch')
class UsuarioRegistroView(CreateView):
    form_class = UsuarioForm
    success_url = reverse_lazy("login")
    template_name = 'usuarios/registro.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('panel')
        return super(UsuarioRegistroView, self).dispatch(request, *args, **kwargs)
    
class UsuarioLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'usuarios/login.html'

class UsuarioLogoutView(LogoutView):
    next_page = reverse_lazy('home')

class UsuarioPanelView(TemplateView):
    template_name = 'usuarios/panel.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movimientos'] = Movimiento.objects.filter(cuenta=self.request.user.id).order_by("-fecha")[:5]
        limite = int(self.request.GET.get('limite', 10))  # Valor dinámico de límite
        context['cuentas'] = Movimiento.objects.cuentas_mas_utilizadas(usuario=self.request.user.id, limite=limite)
        return context

class UsuarioUpdateProfileView(UpdateView):
    form_class = UsuarioUpdateForm
    success_url = reverse_lazy("panel")
    template_name = 'usuarios/perfil.html'

    def get_object(self, queryset: QuerySet[any] | None = ...) -> Model:
        return self.request.user
    
class UsuarioCambiarPasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'usuarios/cambiar_password.html'
    success_url = reverse_lazy("panel")
    success_message = "Contraseña cambiada con exito."

# Administracion de usuarios views
class AdminUsuariosListView(UserPassesTestMixin, FilterView):
    filterset_fields = {
        'username': ['icontains'],
        'is_staff': ['exact'],
    }
    model = Usuario
    paginate_by = 10
    template_name = 'usuarios/admin_list.html'

    def test_func(self):
        return self.request.user.is_staff

class AdminUsuariosUpdateView(SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = Usuario
    form_class = AdminUsuarioUpdateForm
    success_url = reverse_lazy("usuarios:list")
    success_message = "Datos del usuario actualizados con exito."
    template_name = 'usuarios/admin_update.html'

    def get_success_url(self) -> str:
        o = self.object
        if (o.id == self.request.user.id) and not o.is_staff:
            self.success_url = reverse_lazy('panel')
        return super().get_success_url()

    def test_func(self):
        return self.request.user.is_staff
