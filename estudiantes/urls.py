from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_estudiantes, name='lista_estudiantes'),
    path('actualizar-edad/',views.actualizar_edad,name='actualizar_edad'),
]
