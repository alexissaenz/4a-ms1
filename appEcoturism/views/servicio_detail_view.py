from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from appEcoturism.models.servicio import Servicio
from appEcoturism.serializers.servicio_serializer import ServicioSerializer
from django.http import Http404
from rest_framework.views import APIView

class ServicioDetailView(APIView):
    #permission_classes = (IsAuthenticated,)
    
    def get_object(self, pk):
        try:
            return Servicio.objects.get(id=pk)
        except Servicio.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):

        
        obj = self.get_object(pk)
        
        serializer = ServicioSerializer(obj)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = ServicioSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
