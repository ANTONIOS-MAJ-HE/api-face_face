from django.db import models
from django.contrib.auth.models import User

# Modelo de Docente
class Docente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=8)

# Modelo de Curso
class Curso(models.Model):
    imagen = models.ImageField(upload_to='imagenes_cursos/')
    nombre = models.CharField(max_length=100)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    ciclo = models.CharField(max_length=10)

# Modelo de Alumno
class Alumno(models.Model):
    codigo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    cursos = models.ManyToManyField(Curso, through='InscripcionCurso')

# Modelo de Inscripción de Alumno a Curso
class InscripcionCurso(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)

# Modelo de Sesión de Curso
class SesionCurso(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha = models.DateField()
    tema = models.CharField(max_length=200)  # Tema principal de la sesión
    contenido = models.TextField(null=True, blank=True)  # Contenido detallado de la sesión

# Modelo de Asistencia
class Asistencia(models.Model):
    sesion_curso = models.ForeignKey(SesionCurso, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    estado_asistencia = models.CharField(max_length=20, choices=[('asistió', 'Asistió'), ('faltó', 'Faltó'), ('tardanza', 'Tardanza')])
