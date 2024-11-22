from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Movimiento
from .forms import MovimientoForm
from django.db.models import Sum


def crear_movimiento(request):
    if request.method == "POST":
        form = MovimientoForm(request.POST)
        if form.is_valid():
         form.save()
        return redirect("movimientos:historial")
    else:
        form = MovimientoForm()
    return render(request, "movimientos/crear_movimiento.html", {"form": form})

def historial_movimientos(request):
    # movimientos = Movimiento.objects.filter(cuenta=request.user).order_by("-fecha") para un solo usuario
    movimientos_list = Movimiento.objects.all().order_by("-fecha")  
    paginator = Paginator(movimientos_list, 10)  # 10 movimientos por página
    monto_total = movimientos_list.aggregate(Sum('monto'))['monto__sum'] or 0

    page_number = request.GET.get('page', 1)
    movimientos = paginator.get_page(page_number)
    total_paginas = movimientos.paginator.num_pages

    return render(request, "movimientos/historial_movimientos.html", {"movimientos": movimientos, "total_paginas": total_paginas, "monto_total": monto_total})