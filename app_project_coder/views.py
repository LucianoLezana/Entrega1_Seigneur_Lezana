from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def inicio (request):
    return render(request, "app_project_coder\inicio.html")  


def estudiantes (request):
    return render(request, "app_project_coder\estudiantes.html")


def profesores (request):
    return render(request, "app_project_coder\profesores.html")


def cursos (request):
    return render(request, "app_project_coder\cursos.html")
