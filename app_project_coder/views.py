from typing import Dict
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from app_project_coder.models import Cursos, Estudiantes, Profesores
from app_project_coder.forms import *

# Create your views here.


def inicio (request):
    return render(request, "app_project_coder\inicio.html")  


def estudiantes (request):
    return render(request, "app_project_coder\estudiantes.html")


def profesores (request):
    return render(request, "app_project_coder\profesores.html")

#Curso-------------------------------------------------------------------------------------------------------------------------------------------------------------------
def cursos(request):
    cursos = Cursos.objects.all()
    return render(request, "app_project_coder\cursos.html", {'cursos': cursos})


def crear_formulario_curso(request):
    if request.method == "POST":
        formulario_curso = form_curso(request.POST)
        print(formulario_curso)
        if formulario_curso.is_valid:
            informacion = formulario_curso.cleaned_data
            cursos = Cursos(nombre=informacion['nombre'], comision=informacion['comision'])
            cursos.save()
            return render(request, "app_project_coder\inicio.html")

    else:
        formulario_curso = form_curso()
        return render(request, "app_project_coder\crear_cursos.html", {"formulario_curso":formulario_curso})


def busqueda_cursos(request):
    return render(request, "app_project_coder/busqueda_curso.html")


def buscador_cursos(request):
    if request.GET["comision"]:
        comision = request.GET["comision"]
        cursos = Cursos.objects.filter(comision__icontains=comision)
        return render(request, "app_project_coder\cursos.html", {'cursos': cursos})
    else:
        return render(request, "app_project_coder\cursos.html", {'cursos': []})



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
