from django import forms
from Medicion.models import Medicion, Alumno, Mediciongrupo
from django.utils.safestring import mark_safe



class HorizontalRadioRenderer(forms.RadioSelect):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))



class Medicionform(forms.ModelForm):

	class Meta:

		model = Medicion
		fields = [
			#'declaracion',
			'opinion',
		]

		labels = {
			#'declaracion': 'Declaración:',
		}
		widgets = {
			#'declaracion': forms.Select(attrs={'class': 'form-control', 'readonly': 'readonly'}),
			'opinion': forms.RadioSelect(attrs={'renderer': 'HorizontalRadioRenderer'}),
		}


class Alumnoform(forms.ModelForm):

	class Meta:
		model = Alumno
		fields = [
			'nombre',
			'apellido_pat',
			'apellido_mat',
			'email',
			'rut',
			'carrera',
		]
		labels = {
			'nombre': 'Nombres:',
			'apellido_pat': 'Apellido Paterno:',
			'apellido_mat': 'Apellido Materno:',
			'email': 'Email:',
			'rut': 'Rut:',
			'carrera': 'Carrera:',
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Luis Enrique'}),
			'apellido_pat': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Fernández'}),
			'apellido_mat': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Pérez'}),
			'email': forms.EmailInput(attrs={'class': 'form-control', }),
			'rut':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 19271880-5'}),	
			'carrera': forms.Select(attrs={'class': 'form-control'}),	
		}



class Mediciongrupoform(forms.ModelForm):

	class Meta:
		model = Mediciongrupo
		fields = [
			'grupo',
			#'integrante',
			'mail',
		]
		labels = {
			'grupo': 'Grupo:',
			#'integrante': 'Alumno:',
			'mail': 'Ingrese Mail Jefe de Proyecto:',
		}
		widgets = {
			'grupo': forms.Select(attrs={'class': 'form-control'}),
			#'integrante': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Fernández'}),
			'mail': forms.TextInput(attrs={'class': 'form-control'}),
		}