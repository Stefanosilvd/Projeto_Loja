from django.http import HttpResponse

def pagamento_view(request):
    return HttpResponse("Página de forma de pagamento")
