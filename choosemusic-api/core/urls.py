""" URLConf central
Diferente do URLConf dos apps (api/urls.py, por exemplo) que direcionam a requisição dentro do app, o core/urls.py
centraliza as requisições e as roteia para os apps responsáveis pelo tratamento específico de cada rota.
No caso deste projeto:
- `api/v1/` redireciona para o app `api`
- `api-auth/` redireciona para o app `rest_framework`
- `admin/` redireciona para o app de administração do próprio Django
- `docs/` redireciona para o app de documentação do DRF
"""

from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('api.urls', namespace='api')),
]