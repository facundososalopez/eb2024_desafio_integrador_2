from django.urls import path

from .views import UsuarioRegistroView

name_prefix = "usuarios_"

urlpatterns = [
    path("registro/", UsuarioRegistroView.as_view(), name=name_prefix + "register"),
]