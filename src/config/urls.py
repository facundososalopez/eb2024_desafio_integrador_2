from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from . import views

# Vistas de apps.usuarios que quiero que tenga path desde de la raiz
from apps.usuarios import views as usuarios_views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('panel', usuarios_views.UsuarioPanelView.as_view(), name='panel'),
    path('perfil', usuarios_views.UsuarioUpdateProfileView.as_view(), name='profile'),
    path('registro', usuarios_views.UsuarioRegistroView.as_view(), name='register'),
    path('login', usuarios_views.UsuarioLoginView.as_view(), name='login'),
    path('logout', usuarios_views.UsuarioLogoutView.as_view(), name='logout'),
    # Reset password
    path('resetear-password/', usuarios_views.UsuarioResetearPasswordView.as_view(), name='password_reset'),
    path('resetear-password/done', usuarios_views.UsuarioResetearPasswordDoneView.as_view(), name='password_reset_done'),
    path('resetear-password/confirm/<uidb64>/<token>/', usuarios_views.UsuarioResetearPasswordConfirmView.as_view(), name='password_reset_confirm'),
    path('resetear-password/complete', usuarios_views.UsuarioResetearPasswordCompleteView.as_view(), name='password_reset_complete'),
    # Fin reset password
    path('cambiar-password/', usuarios_views.UsuarioCambiarPasswordView.as_view(), name='cambiar-password'),
    path('transferencia_motivo/', include('apps.transferencia_motivo.urls')),
    path('usuarios/', include('apps.usuarios.urls')),
    path('movimientos/', include('apps.movimientos.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
