from django.shortcuts import render
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.
class UsuarioRegistroView(CreateView):
    form_class = UsuarioForm
    success_url = reverse_lazy("login")
    template_name = 'usuarios/registro.html'
