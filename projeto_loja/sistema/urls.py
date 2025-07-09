from django.urls import path
from .views import forma_pagamento, confirmacao

urlpatterns = [
    path("forma_pagamento/", forma_pagamento, name="forma_pagamento"),
    path("confirmacao/", confirmacao, name="confirmacao"),
]
