from django.urls import path

from .views import AdminUsuariosListView, AdminUsuariosUpdateView

app_name = 'usuarios'

urlpatterns = [
    path('', AdminUsuariosListView.as_view(), name="list"),
    path('<int:pk>/editar', AdminUsuariosUpdateView.as_view(), name="update"),
]