from django.urls import path
from . import views
from .views import (
   Transferencia,
   HistorialMovimientos,
)

app_name = "movimientos"

urlpatterns = [
    path("crear/", views.crear_movimiento, name="crear"),
     path('historial/', HistorialMovimientos.as_view(), name='historial'),
    path('transferencia/', Transferencia.as_view(), name='transferencia'),
]