from rest_framework import status, views
from rest_framework.response import Response

from appEcoturism.serializers.tipo_servicio_serializer import TipoServicioSerializer


class TipoServCreateView(views.APIView):
    def post(self, request):
        serializer = TipoServicioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        
        if serializer.is_valid():
            obj = serializer.save()
            if obj:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)