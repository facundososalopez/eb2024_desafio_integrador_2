from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from .forms import UsuarioForm, UsuarioUpdateForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_not_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from apps.movimientos.models import Movimiento

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

class UsuarioUpdateProfileView(UpdateView):
    form_class = UsuarioUpdateForm
    success_url = reverse_lazy("panel")
    template_name = 'usuarios/perfil.html'

    def get_object(self, queryset: QuerySet[any] | None = ...) -> Model:
        return self.request.user
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movimientos'] = Movimiento.objects.filter(cuenta=self.request.user.id).order_by("-fecha")[:5]
        return context
