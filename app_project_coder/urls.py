from django.urls import path
from app_project_coder import views


urlpatterns = [

    path('', views.inicio, name="Inicio"),
    path('estudiantes/', views.estudiantes, name="Estudiantes"),
    path('profesores/', views.profesores, name="Profesores"),
    path('cursos/', views.cursos, name="Cursos"),



]