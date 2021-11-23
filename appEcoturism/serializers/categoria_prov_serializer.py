from django.db import models
from appEcoturism.models.categoria_prov import Categoria_Prov
from rest_framework import serializers

class CategoriaProvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria_Prov
        fields = ['id', 'nombre']
        read_only_fields = ['id']