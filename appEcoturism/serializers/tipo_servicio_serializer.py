from django.db import models
from appEcoturism.models.tipo_servicio import Tipo_Servicio
from rest_framework import serializers

class TipoServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Servicio
        fields = ['id', 'nombre']