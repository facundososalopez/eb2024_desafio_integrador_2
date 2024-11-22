from django.urls import path
from . import views

app_name = "movimientos"

urlpatterns = [
    path("crear/", views.crear_movimiento, name="crear"),
    path("historial/", views.historial_movimientos, name="historial"),
]