from django.urls import path
from .views import (
   Transferencia,
   HistorialMovimientos,
   IngresoDinero,
   TransferenciaCuenta,
   MovimientoDetailView,
   HistorialMovimientosAdmin
)

app_name = "movimientos"

urlpatterns = [
    path("historial/", HistorialMovimientos.as_view(), name="historial"),
    path('transferencia/', Transferencia.as_view(), name='transferencia'),
    path("ingreso_dinero/", IngresoDinero.as_view(), name="ingreso_dinero"),
    path('transferencia_cuenta/<int:cuenta_asociada_id>/', TransferenciaCuenta.as_view(), name='transferencia_cuenta'),
    path('movimiento_detail/<int:pk>/', MovimientoDetailView.as_view(), name='movimiento_detail'),
    path("admin_historial/", HistorialMovimientosAdmin.as_view(), name="admin_historial"),
]