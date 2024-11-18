from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import MotivoTransferencia

class MotivoListView(ListView):
    model = MotivoTransferencia
    template_name = 'transferencia_motivo/motivo_list.html'
    context_object_name = 'motivos'

class MotivoCreateView(CreateView):
    model = MotivoTransferencia
    fields = ['descripcion']
    template_name = 'transferencia_motivo/motivo_form.html'
    success_url = reverse_lazy('transferencia_motivo:list')

class MotivoUpdateView(UpdateView):
    model = MotivoTransferencia
    fields = ['descripcion']
    template_name = 'transferencia_motivo/motivo_form.html'
    success_url = reverse_lazy('transferencia_motivo:list')

class MotivoDeleteView(DeleteView):
    model = MotivoTransferencia
    template_name = 'transferencia_motivo/motivo_confirm_delete.html'
    success_url = reverse_lazy('transferencia_motivo:list')

