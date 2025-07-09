from django.urls import path
from .views import pagamento_view

urlpatterns = [
    path('', pagamento_view, name='pagamento'),
]
