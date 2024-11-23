from django.shortcuts import render, redirect
from django.views.generic import ListView
from apps.transferencia_motivo.models import MotivoTransferencia
from apps.usuarios.models import Usuario
from .models import Movimiento
from .forms import MovimientoForm
from django.shortcuts import render, get_object_or_404
from django.db import transaction
from django.contrib import messages
from .forms import TransferenciaForm 
from django.http import HttpResponseRedirect
from django.views.generic import FormView
from django.urls import reverse





def crear_movimiento(request):
    if request.method == "POST":
        form = MovimientoForm(request.POST)
        if form.is_valid():
         form.save()
        return redirect("movimientos:historial")
    else:
        form = MovimientoForm()
    return render(request, "movimientos/crear_movimiento.html", {"form": form})

class HistorialMovimientos(ListView):
    model = Movimiento
    template_name = "movimientos/historial_movimientos.html"
    context_object_name = "movimientos"
    paginate_by = 10 # Número de elementos por página

    def get_queryset(self):
        # Filtrar movimientos por el usuario logueado
        return Movimiento.objects.filter(cuenta=self.request.user.id).order_by("-fecha")

    def get_context_data(self, **kwargs):
        # Agregar datos adicionales al contexto
        context = super().get_context_data(**kwargs)
        context["total_paginas"] = context["paginator"].num_pages
        context["monto_total"] = self.request.user.saldo
        return context

class Transferencia(FormView):
    template_name = 'movimientos/transferencia.html'
    form_class = TransferenciaForm # Asociar el formulario creado

    def form_valid(self, form):
        # Recuperar los datos del formulario
        cuenta_asociada_id = form.cleaned_data['cuenta_asociada_id'].id  # Asumiendo que el campo se llama 'cuenta_asociada_id' en el formularioT['cuenta_asociada_id']
       
        monto = form.cleaned_data['monto']
        transferencia_motivo = form.cleaned_data['transferencia_motivo']

        # Obtener el usuario origen (el usuario logueado)
        usuario_origen = get_object_or_404(Usuario, pk=self.request.user.id)
        usuario_destino = get_object_or_404(Usuario, pk=cuenta_asociada_id)

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
        motivos = MotivoTransferencia.objects.all()  # Obtener todos los motivos
        usuarios = Usuario.objects.exclude(id=self.request.user.id)  # Excluir el usuario logueado
        return self.render_to_response(self.get_context_data(form=form, usuarios=usuarios, motivos=motivos))

    def get_form_kwargs(self):
        # Llama a los kwargs del formulario estándar
        kwargs = super().get_form_kwargs()
        # Agrega el usuario logueado al formulario
        kwargs['user'] = self.request.user
        return kwargs


