from rest_framework.settings import perform_import
from appEcoturism.models.user import User
from appEcoturism.models.perfil import Perfil
from rest_framework import serializers
from appEcoturism.serializers.perfil_serializer import PerfilSerializer


class UserSerializer(serializers.ModelSerializer):
    perfil = PerfilSerializer()
    class Meta:
        model = User
        fields = ['username', 'password', 'name', 'email', 'perfil']

    def create(self, validated_data):
        perfil_data = validated_data.pop('perfil')
        user_instance = User.objects.create(**validated_data)
        Perfil.objects.create(user=user_instance, **perfil_data)
        return user_instance
    
    def update(self, instance, validated_data):
        perfil_data = validated_data.pop('perfil')

        perfil = Perfil.objects.get(user=instance.id)

        perfil.ciudad = perfil_data.get('ciudad', perfil.ciudad)
        perfil.celular = perfil_data.get('celular', perfil.celular)
        perfil.direccion = perfil_data.get('direccion', perfil.direccion)
        perfil.imagen = perfil_data.get('imagen', perfil.imagen)
        perfil.save()
        
        return instance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        perfil = Perfil.objects.get(user=obj.id)
        return {
            'id': user.id, 
            'username': user.username, 
            'name': user.name, 
            'email': user.email, 
            'perfil': {
                'id': perfil.id,
                'numDoc': perfil.num_doc, 
                'ciudad': perfil.ciudad, 
                'celular': perfil.celular,
                'direccion': perfil.direccion,
                'activo': perfil.activo,
                'imagen': perfil.imagen
            }
        }