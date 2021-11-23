from rest_framework.settings import perform_import
from appEcoturism.models.user import User
from appEcoturism.models.proveedor import Proveedor
from rest_framework import serializers


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ['id', 'nit', 'cat_prov', 'nombre', 'direccion', 'ciudad', 'activo', 'imagen']
        read_only_fields = ['id']