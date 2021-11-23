from django.db import models
from appEcoturism.models.perfil import Perfil
from rest_framework import serializers


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ['id', 'num_doc', 'ciudad', 'celular', 'direccion', 'activo', 'imagen']
        read_only_fields = ['id']