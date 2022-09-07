from socket import fromshare
from django import forms

#Crear formularios para la pagina

#Formulario Cursos:
class form_curso(forms.Form):
    nombre = forms.CharField(max_length=120)
    comision = forms.IntegerField()

#-------------------

#Formulario Estudiantes:
class form_estudiantes(forms.Form): 
    nombre = forms.CharField(max_length=120)
    apellido = forms.CharField(max_length=120)
    email = forms.EmailField()

#-------------------

#Formulario Profesores:
class form_profesores(forms.Form):
    nombre = forms.CharField(max_length=120)
    apellido = forms.CharField(max_length=120)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=100)

#-------------------



