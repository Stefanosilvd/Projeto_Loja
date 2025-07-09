from django.shortcuts import render, redirect
from .models import Pagamento

def forma_pagamento(request):
    if request.method == "POST":
        forma = request.POST.get("forma_pagamento")
        if forma:
            Pagamento.objects.create(forma=forma)
            return redirect('confirmacao')  # redireciona para a próxima página
    return render(request, "pagamento.html")

def confirmacao(request):
    return render(request, "confirmacao.html")