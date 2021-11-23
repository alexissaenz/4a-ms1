from functools import partial
from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from appEcoturism.models.user import User
from appEcoturism.serializers.user_serializer import UserSerializer
from django.http import Http404
from rest_framework.views import APIView

class UserDetailView(APIView):
    #permission_classes = (IsAuthenticated,)
    
    def get_object(self, pk):
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):

        
        obj = self.get_object(pk)
        
        serializer = UserSerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = UserSerializer(obj, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)