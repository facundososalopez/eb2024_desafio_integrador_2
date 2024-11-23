from django.urls import path
from .views import (
   Transferencia,
   HistorialMovimientos,
   IngresoDinero
)

app_name = "movimientos"

urlpatterns = [
    path("historial/", HistorialMovimientos.as_view(), name="historial"),
    path('transferencia/', Transferencia.as_view(), name='transferencia'),
    path("ingreso_dinero/", IngresoDinero.as_view(), name="ingreso_dinero"),
]