from django.shortcuts import redirect
from django.views.generic import ListView
from apps.transferencia_motivo.models import MotivoTransferencia
from apps.usuarios.models import Usuario
from .models import Movimiento, MovimientoFilter, MovimientoAdmin, MovimientoAdminFilter
from .forms import IngresoDineroForm, TransferenciaCuentaForm
from django.shortcuts import get_object_or_404
from django.db import transaction
from django.contrib import messages
from .forms import TransferenciaForm 
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from django.urls import reverse
from django.views.generic.detail import DetailView
from django_filters.views import FilterView

from config.mixins import TestStaffMixin

class HistorialMovimientos(FilterView):
    model = Movimiento
    template_name = "movimientos/mi_historial_movimientos.html"
    context_object_name = "movimientos"
    paginate_by = 10 # Número de elementos por página
    filterset_class = MovimientoFilter

    def get_queryset(self):
        # Filtrar movimientos por el usuario logueado
        return Movimiento.objects.filter(cuenta=self.request.user.id).order_by("-fecha")

    def get_context_data(self, **kwargs):
        # Agregar datos adicionales al contexto
        context = super().get_context_data(**kwargs)
        context["total_paginas"] = context["paginator"].num_pages
        context["monto_total"] = self.request.user.saldo  
        return context

class HistorialMovimientosAdmin(TestStaffMixin, FilterView):
    model = MovimientoAdmin
    template_name = "movimientos/admin_historial_movimientos.html"
    context_object_name = "movimientos"
    paginate_by = 10 # Número de elementos por página
    filterset_class = MovimientoAdminFilter

    def get_queryset(self):
        return Movimiento.objects.all().order_by("-fecha")

class Transferencia(FormView):
    template_name = 'movimientos/transferencia.html'
    form_class = TransferenciaForm

    def form_valid(self, form):
 
        cuenta_asociada_id = form.cleaned_data['cuenta_asociada_id']
        print(cuenta_asociada_id) # 
       
        monto = form.cleaned_data['monto']
        transferencia_motivo = form.cleaned_data['transferencia_motivo']

        # Obtener el usuario origen (el usuario logueado)
        usuario_origen = get_object_or_404(Usuario, pk=self.request.user.id)
        usuario_destino = get_object_or_404(Usuario, pk=cuenta_asociada_id.id)

        #mostrar en consola usuarios
        print("Usuario origen:", usuario_origen)
        print("Usuario destino:", usuario_destino)

        # Verificar si hay suficiente saldo
        if usuario_origen.saldo < monto:
            messages.error(self.request, "Saldo insuficiente.")
            return self.form_invalid(form)

        try:
            with transaction.atomic():
                # Actualizar saldos
                usuario_origen.saldo -= monto
                usuario_origen.save()

                usuario_destino.saldo += monto
                usuario_destino.save()

                # Registrar movimientos
                Movimiento.objects.create(
                    cuenta=usuario_origen,  # Emisor
                    cuenta_asociada=usuario_destino,  # Receptor
                    tipo='2',  # Transferencia realizada
                    monto=monto,
                    transferencia_motivo=transferencia_motivo,
                )

                Movimiento.objects.create(
                    cuenta=usuario_destino,  # Receptor
                    cuenta_asociada=usuario_origen,  # Emisor
                    tipo='3',  # Transferencia recibida
                    monto=monto,
                    transferencia_motivo=transferencia_motivo,
                )

            messages.success(self.request, "Transferencia realizada con éxito.")
            return HttpResponseRedirect(reverse('panel'))

        except Exception as e:
            messages.error(self.request, f"Error al realizar la transferencia: {str(e)}")
            return self.form_invalid(form)

    def form_invalid(self, form):
        # Esta función maneja lo que ocurre si el formulario es inválido
        motivos = MotivoTransferencia.objects.all()  
        usuarios = Usuario.objects.exclude(id=self.request.user.id)
        return self.render_to_response(self.get_context_data(form=form, usuarios=usuarios, motivos=motivos))

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

class TransferenciaCuenta(FormView):
    template_name = 'movimientos/transferencia_cuenta.html'
    form_class = TransferenciaCuentaForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        cuenta_id = self.kwargs.get('cuenta_asociada_id')
        kwargs['cuenta_asociada_id'] = cuenta_id  
        kwargs['user'] = self.request.user  
        return kwargs

class IngresoDinero(FormView):
    template_name = "movimientos/ingreso_dinero.html"
    form_class = IngresoDineroForm

    def form_valid(self, form):
        monto = form.cleaned_data["monto"]
        usuario = self.request.user  # Usuario logueado

        try:
            with transaction.atomic():
                usuario.saldo += monto
                usuario.save()

                Movimiento.objects.create(
                    cuenta=usuario,
                    cuenta_asociada=None,
                    tipo="1",
                    monto=monto,
                )

            messages.success(self.request, f"Se han ingresado ${monto:.2f} a tu cuenta.")
        except Exception as e:
            messages.error(self.request, f"Error al realizar el ingreso: {str(e)}")

        return redirect("panel")

    def form_invalid(self, form):
        messages.error(self.request, "Por favor corrige los errores del formulario.")
        return super().form_invalid(form)

class MovimientoDetailView(DetailView):
    model = Movimiento
    template_name = 'movimientos/movimiento_detail.html'
    context_object_name = 'movimiento'



