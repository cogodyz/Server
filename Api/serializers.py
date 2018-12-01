from .models import Perrito
from rest_framework import serializers


class PerritosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perrito
        fields = ( 'id','foto', 'nombre', 'raza', 'descripcion', 'estado')
