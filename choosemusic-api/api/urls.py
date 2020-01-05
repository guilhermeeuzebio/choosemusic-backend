""" URLConf do app `api`
Configura as rotas e redireciona as requisições para as Views que as tratarão
"""
from django.urls import include, path
from rest_framework import routers
from api import views

app_name = 'api'

# Router padrão
router = routers.DefaultRouter()
router.register(r'music', views.MusicViewSet, basename='music')

# Padrões de URL
urlpatterns = [
    path('', include(router.urls)),
]