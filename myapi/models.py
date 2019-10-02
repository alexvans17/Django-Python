from django.db import models

class Tienda(models.Model):
	id_tienda = models.CharField(max_length=10, primary_key=True)
	nombre = models.CharField(max_length=120)

	def __str__(self):
		return self.nombre

class Categoria(models.Model):
	id_categoria = models.CharField(max_length=10, primary_key=True)
	descripcion = models.CharField(max_length=100)

	def __str__(self):
		return self.descripcion

class Producto(models.Model):
	id_producto = models.CharField(max_length=10)
	nombre_producto = models.CharField(max_length=100)
	cantidad = models.CharField(max_length=10)
	precio = models.DecimalField(max_digits=10, decimal_places=2)
	id_categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING,)
	id_tienda = models.ForeignKey(Tienda, on_delete=models.DO_NOTHING,)

	def __str__(self):
		return self.nombre_producto

class Cliente(models.Model):

	id_cliente = models.CharField(max_length=120, primary_key=True)
	nombre = models.CharField(max_length=120)
	apellido = models.CharField(max_length=120)
	usuario = models.CharField(max_length=120)
	password = models.CharField(max_length=100)	

	def __str__(self):
		return self.usuario

class Venta(models.Model):

	def obtenerProductosXCliente(id_cliente):
		pass

	def registrarVenta(id_producto, id_cliente):
		pass
		
		