from .models import Perrito
from rest_framework import viewsets
from Api.serializers import PerritosSerializer


class PerritosViewSet(viewsets.ModelViewSet):
    queryset = Perrito.objects.all()
    serializer_class = PerritosSerializer
