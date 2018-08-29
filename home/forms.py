from django import forms 
from .models import *
from django.contrib.auth.models import User

class contacto_form (forms.Form):
	correo = forms.EmailField(widget=forms.TextInput())
	asunto = forms.CharField(widget=forms.TextInput())
	texto  = forms.CharField(widget=forms.Textarea())

class agregar_producto_form (forms.ModelForm):
	class Meta:
		model = Producto 
		fields = '__all__'

class login_form (forms.Form):
	usuario = forms.CharField(widget=forms.TextInput())
	clave 	= forms.CharField(widget=forms.PasswordInput(render_value=False))

class register_form(forms.Form):
	usuario = forms.CharField(widget=forms.TextInput())
	correo 	= forms.EmailField(widget=forms.TextInput())
	clave_1	= forms.CharField(widget=forms.PasswordInput(render_value=False))
	clave_2	= forms.CharField(widget=forms.PasswordInput(render_value=False))

	def clean_usuario (self):
		usuario = self.cleaned_data['usuario']
		try:
			u = User.objects.get(username = usuario)
		except User.DoesNotExist:
			return usuario 
		raise forms.ValidationError('Usuario ya registrado')

	def clean_correo (self):
		correo = self.cleaned_data['correo']
		try:
			u = User.objects.get(email = correo)
		except User.DoesNotExist:
			return correo
		raise forms.ValidationError('El correo ya esta registrado')

	def clean_clave_2 (self):
		clave_1 = self.cleaned_data['clave_1']
		clave_2 = self.cleaned_data['clave_2']
		if clave_1 == clave_2:
			pass
		else:
			raise forms.ValidationError('las Claves no coinciden')
