from django.db import models
from .categoria_prov import Categoria_Prov

class Proveedor(models.Model):
    nit = models.CharField('num_doc', max_length = 20)
    cat_prov = models.ForeignKey(Categoria_Prov, related_name='proveedor', on_delete=models.CASCADE)
    nombre = models.CharField('nombre', max_length = 100)
    direccion = models.CharField('direccion', max_length = 100)
    ciudad = models.CharField('ciudad', max_length = 50)
    activo = models.BooleanField(default=False)
    imagen = models.CharField('imagen', max_length = 250)