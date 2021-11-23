from django.contrib import admin

# Register your models here.
from .models.user import User
from .models.perfil import Perfil
from .models.categoria_prov import Categoria_Prov
from .models.plan import Plan
from .models.proveedor import Proveedor
from .models.servicio import Servicio
from .models.tipo_servicio import Tipo_Servicio

admin.site.register(User)
admin.site.register(Perfil)
admin.site.register(Categoria_Prov)
admin.site.register(Plan)
admin.site.register(Proveedor)
admin.site.register(Servicio)
admin.site.register(Tipo_Servicio)


