from django.urls import path
from .views import (
    MotivoListView,
    MotivoCreateView,
    MotivoUpdateView,
    MotivoDeleteView,
)

app_name = 'transferencia_motivo'

urlpatterns = [
    path('', MotivoListView.as_view(), name='list'),
    path('crear/', MotivoCreateView.as_view(), name='create'),
    path('<int:pk>/editar/', MotivoUpdateView.as_view(), name='update'),
    path('<int:pk>/eliminar/', MotivoDeleteView.as_view(), name='delete'),
]