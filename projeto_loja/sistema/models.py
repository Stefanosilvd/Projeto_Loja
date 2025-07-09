from django.db import models

# Create your models here.
from django.db import models

class Pagamento(models.Model):
    FORMA_CHOICES = [
        ('cartao', 'Cartão de Crédito'),
        ('pix', 'Pix'),
        ('boleto', 'Boleto'),
    ]

    forma = models.CharField(max_length=10, choices=FORMA_CHOICES)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.forma} - {self.criado_em.strftime("%d/%m/%Y %H:%M")}'
