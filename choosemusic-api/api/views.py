from rest_framework import viewsets

from api.serializers import MusicSerializer
from core.models import Music


class MusicViewSet(viewsets.ModelViewSet):
    """
    ViewSet that allows to do the following operations under entity `Music`:
    `create()`, `retrieve()`, `update()`, `partial_update()`, `destroy()` e `list()`
    """
    queryset = Music.objects.all()
    serializer_class = MusicSerializer