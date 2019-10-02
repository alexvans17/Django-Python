from rest_framework import serializers

from .models import Tienda, Categoria, Producto, Cliente

class TiendaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tienda
        fields = ('id_tienda', 'nombre')

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id_categoria', 'descripcion')

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = ('id_producto', 'nombre_producto','cantidad','precio','id_categoria', 'id_tienda')

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id_cliente', 'nombre', 'apellido', 'usuario', 'password')
