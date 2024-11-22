"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from . import views

# Vistas de apps.usuarios que quiero que tenga path desde de la raiz
from apps.usuarios import views as usuarios_views

urlpatterns = [
    path('base', views.BaseTemplateView.as_view(), name='base'),
    path('', views.HomeView.as_view(), name='home'),
    path('panel', usuarios_views.UsuarioPanelView.as_view(), name='panel'),
    path('admin/', admin.site.urls),
    path('registro', usuarios_views.UsuarioRegistroView.as_view(), name='register'),
    path('login', usuarios_views.UsuarioLoginView.as_view(), name='login'),
    path('logout', usuarios_views.UsuarioLogoutView.as_view(), name='logout'),
    path('transferencia_motivo/', include('apps.transferencia_motivo.urls')),
    path('usuarios/', include('apps.usuarios.urls')),
    path('movimientos/', include('apps.movimientos.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
