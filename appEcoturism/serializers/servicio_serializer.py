from rest_framework.settings import perform_import
from appEcoturism.models.user import User
from appEcoturism.models.servicio import Servicio
from rest_framework import serializers


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ['id', 'nombre', 'activo', 'imagen', 'precio', 'proveedor', 'tipo_serv', 'plan']
        read_only_fields = ['id']