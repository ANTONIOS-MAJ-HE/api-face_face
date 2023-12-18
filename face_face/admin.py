from django.contrib import admin
from .models import User, Alumno, SesionCurso, InscripcionCurso, Docente, Asistencia, Curso
# Register your models here.

admin.site.register(Docente)
admin.site.register(Curso)
admin.site.register(Alumno)
admin.site.register(InscripcionCurso)
admin.site.register(SesionCurso)
admin.site.register(Asistencia)