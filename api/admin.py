from django.contrib import admin

from .models import Usuario
from .models import Lista
from .models import Tienda
from .models import Producto

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Lista)
admin.site.register(Tienda)
admin.site.register(Producto)

