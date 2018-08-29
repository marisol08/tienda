from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Marca (models.Model):
	nombre 	= models.CharField(max_length=100)

	def __str__ (self):
		return self.nombre

class Categoria (models.Model):
	nombre 	= models.CharField(max_length=100)

	def __str__ (self):
		return self.nombre

class Producto (models.Model):
	nombre 	= models.CharField(max_length=100)
	precio 	= models.IntegerField()
	stock 	= models.IntegerField()
	status 	= models.BooleanField(default=True)
	foto 	= models.ImageField(upload_to='fotos', null=True, blank=True)
	marca 	= models.ForeignKey(Marca, on_delete=models.PROTECT)
	categoria = models.ManyToManyField(Categoria, null=True, blank=True)

	def __str__(self):
		return self.nombre + ' ' +str(self.precio)

class Perfil (models.Model):
	GENERO = ( 	('femenino','Femenino'),
				('masculino','Masculino'),
		)
	imagen 		= models.ImageField(upload_to='perfiles', null=True, blank=True)
	telefono	= models.CharField(max_length=100)
	genero 		= models.CharField(max_length=15, choices=GENERO)
	user 		= models.OneToOneField(User, on_delete=models.PROTECT)

	def __str__ (self):
		return self.telefono + ' ' + str(self.user.username)