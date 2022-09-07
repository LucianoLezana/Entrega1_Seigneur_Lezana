from django.urls import path
from app_project_coder import views


urlpatterns = [

    path('', views.inicio, name="Inicio"),
    path('estudiantes/', views.estudiantes, name="Estudiantes"),
    path('profesores/', views.profesores, name="Profesores"),
    # PATH DE CURSOS---------------------------------------------------------------------------
    path('cursos/', views.cursos, name="Cursos"),
    path('crear_cursos/', views.crear_formulario_curso, name="crear_cursos"),
    path('buscar_curso/', views.busqueda_cursos, name="buscar_curso"),
    path('busqueda_curso/', views.buscador_cursos, name="busqueda_curso"),
    #------------------------------------------------------------------------------------------



]