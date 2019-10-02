from django.contrib import admin

from .models import Tienda, Categoria, Producto, Cliente

# Register your models here.
admin.site.register(Tienda)
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Cliente)