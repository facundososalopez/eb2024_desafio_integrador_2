from django.shortcuts import render, redirect
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
class UsuarioRegistroView(CreateView):
    form_class = UsuarioForm
    success_url = reverse_lazy("login")
    template_name = 'usuarios/registro.html'
    
class UsuarioLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'usuarios/login.html'

class UsuarioLogoutView(LogoutView):
    next_page = reverse_lazy('home')

class UsuarioPanelView(TemplateView):
    template_name = 'usuarios/panel.html'