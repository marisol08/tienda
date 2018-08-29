from django.shortcuts import render, redirect 
from django.contrib.auth import login, logout, authenticate
from .forms import *
from .models import *
# Create your views here.

def inicio_view (request):
	return render(request, 'inicio.html', locals())
	
def quienes_somos_view(request):
	nombre = [12,3,45,67,89,436,51]
	#return render(request, 'quienes_somos.html', {'n':nombre})
	return render(request, 'quienes_somos.html', locals())

def contacto_view(request):
	email=""
	subject=""
	text=""
	info_enviado = False
	if request.method=='POST':
		formulario = contacto_form(request.POST)
		if formulario.is_valid():
			email  	= formulario.cleaned_data['correo'] 
			subject = formulario.cleaned_data['asunto']
			text 	= formulario.cleaned_data['texto']
			info_enviado = True
			return render(request, 'contacto.html', locals())
		else:
			msg = 'la informacion no es correcta'	
	else: # si es un metodo GET		
		formulario = contacto_form()
	return render(request, 'contacto.html', locals())


def lista_productos_view (request):
	lista = Producto.objects.filter(status=True)
	return render(request, 'lista_productos.html', locals())

def agregar_producto_view (request):
	accion = 'Agregar'
	if request.user.is_authenticated and request.user.is_superuser:		
		if request.method == 'POST':
			formulario = agregar_producto_form(request.POST, request.FILES)	
			if formulario.is_valid():
				formulario.save()
				return redirect('/lista_productos/')
			else:
				msj = "hay datos no validos"	 
		else:
			formulario = agregar_producto_form()
		return render(request, 'agregar_producto.html', locals())
	else:
		return redirect('/lista_productos/')
		
def ver_producto_view(request, id_prod):
	try:
		obj = Producto.objects.get(id = id_prod)
	except:
		print ("Error en la consulta el Producto no existe")
		msj = "Error en la consulta el Producto no existe"
	return render(request, 'ver_producto.html', locals())

def editar_producto_view(request, id_prod):
	accion = 'Editar'
	obj = Producto.objects.get(id = id_prod)
	if request.method == 'POST':
		formulario = agregar_producto_form(request.POST, request.FILES, instance=obj)
		if formulario.is_valid():
			formulario.save()
			return redirect('/lista_productos/')
	formulario = agregar_producto_form(instance=obj)
	return render(request, 'agregar_producto.html', locals())

def eliminar_producto_view (request, id_prod):
	obj = Producto.objects.get(id = id_prod)
	obj.delete()
	return redirect('/lista_productos/')

def desactivar_producto_view (request,id_prod):
	obj = Producto.objects.get(id = id_prod)
	obj.status = False
	obj.save()
	return redirect('/lista_productos/')

def login_view (request):
	if request.method == 'POST':
		formulario = login_form(request.POST)
		if formulario.is_valid():
			user = formulario.cleaned_data['usuario']
			cla = formulario.cleaned_data['clave']
			usuario = authenticate(username = user, password = cla)
			if usuario is not None and usuario.is_active:
				login(request, usuario)
				return redirect('/lista_productos/') 
			else:
				msj = 'usuario o clave incorrectos'	
	formulario = login_form()
	return render(request, 'login.html', locals())

def logout_view (request):
	logout(request)
	return redirect('/login/')

def register_view (request):
	formulario = register_form()
	usu = ""
	cor = ""
	cla_1 = ""
	cla_2 =""
	if request.method=='POST':
		formulario = register_form(request.POST)
		if formulario.is_valid():
			usu   = formulario.cleaned_data['usuario']
			cor   = formulario.cleaned_data['correo']
			cla_1 = formulario.cleaned_data['clave_1']
			cla_2 = formulario.cleaned_data['clave_2']
			u = User.objects.create_user(username = usu, email=cor, password=cla_1)
			u.save()
			return redirect ('/login/')
		else:
			msj = 'no se pudo crear el usuario'			
	else:		
		return render(request, 'register.html', locals())
	return render(request, 'register.html', locals())

from django.http import HttpResponse 
from django.core import serializers 

def servicio_web_view (request):
	data = serializers.serialize('xml', Producto.objects.all())
	return HttpResponse(data, content_type = 'application/xml' )

