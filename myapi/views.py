from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .serializers import TiendaSerializer, CategoriaSerializer, ProductoSerializer,ClienteSerializer
from .models import Tienda, Categoria, Producto, Cliente

class TiendaViewSet(viewsets.ModelViewSet):
	queryset = Tienda.objects.all().order_by('id_tienda')
	serializer_class = TiendaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by('id_categoria')
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
	queryset = Producto.objects.all().order_by('id_producto')
	serializer_class = ProductoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
	queryset = Cliente.objects.all().order_by('id_cliente')
	serializer_class = ClienteSerializer

class HelloView(APIView):
	permission_classes = (IsAuthenticated,)             # <-- And here

	def get(self, request):
		content = {'message': 'Hello, World!'}
		return Response(content)