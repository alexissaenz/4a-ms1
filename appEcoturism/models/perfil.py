from django.db import models
from .user import User

class Perfil(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='perfil', on_delete=models.CASCADE)
    num_doc = models.CharField('num_doc', max_length = 20)
    ciudad = models.CharField('ciudad', max_length = 50)
    celular = models.CharField('celular', max_length = 100)
    direccion = models.CharField('direccion', max_length = 100)
    activo = models.BooleanField(default=False)
    imagen = models.CharField('imagen', max_length = 250)