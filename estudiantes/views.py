from django.shortcuts import render, get_object_or_404, redirect
from .models import Estudiante

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    cantidad = Estudiante.objects.count()

    return render(
        request,
        'estudiantes/lista.html',
        {'estudiantes': estudiantes, 'cantidad': cantidad}
    )


def actualizar_edad(request):

    mensaje = None

    if request.method == 'POST':
        correo = request.POST.get('correo')
        nueva_edad = request.POST.get('edad')

        estudiante = get_object_or_404(
            Estudiante,
            correo=correo
        )

        estudiante.edad = nueva_edad
        estudiante.save()

        mensaje = '¡Edad actualizada correctamente! 🎉'

    return render(
        request,
        'estudiantes/actualizar_edad.html',
        {'mensaje': mensaje}
    )
