from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import MotivoTransferencia
from .forms import MotivoTransferenciaForm
from django.contrib.messages.views import SuccessMessageMixin
from config.mixins import TestStaffMixin

class MotivoListView(TestStaffMixin, ListView):
    model = MotivoTransferencia
    template_name = 'transferencia_motivo/motivo_list.html'
    context_object_name = 'motivos'

class MotivoCreateView(TestStaffMixin,SuccessMessageMixin, CreateView):
    model = MotivoTransferencia
    form_class = MotivoTransferenciaForm
    template_name = 'transferencia_motivo/motivo_form.html'
    success_url = reverse_lazy('transferencia_motivo:list')
    success_message = "Guardado con éxito."

class MotivoUpdateView(TestStaffMixin, SuccessMessageMixin, UpdateView):
    model = MotivoTransferencia
    fields = ['descripcion']
    template_name = 'transferencia_motivo/motivo_form.html'
    success_url = reverse_lazy('transferencia_motivo:list')
    success_message = "Guardado con éxito."

class MotivoDeleteView(TestStaffMixin,SuccessMessageMixin, DeleteView):
    model = MotivoTransferencia
    template_name = 'transferencia_motivo/motivo_confirm_delete.html'
    success_url = reverse_lazy('transferencia_motivo:list')
    success_message = "Borrado con éxito."

