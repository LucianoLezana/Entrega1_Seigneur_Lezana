from socket import fromshare
from django import forms


#Crear formularios para la pagina


class form_curso(forms.Form):
    nombre = forms.CharField(max_length=120)
    comision = forms.IntegerField()


