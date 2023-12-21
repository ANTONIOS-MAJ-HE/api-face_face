# Generated by Django 5.0 on 2023-12-18 20:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=8)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='imagenes_cursos/')),
                ('nombre', models.CharField(max_length=100)),
                ('ciclo', models.CharField(max_length=10)),
                ('docente', models.ForeignKey(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='InscripcionCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inscripcion', models.DateField(auto_now_add=True)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='face_face.alumno')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='face_face.curso')),
            ],
        ),
        migrations.AddField(
            model_name='alumno',
            name='cursos',
            field=models.ManyToManyField(through='face_face.InscripcionCurso', to='face_face.curso'),
        ),
        migrations.CreateModel(
            name='SesionCurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('tema', models.CharField(max_length=200)),
                ('contenido', models.TextField(blank=True, null=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='face_face.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_asistencia', models.CharField(choices=[('asistió', 'Asistió'), ('faltó', 'Faltó'), ('tardanza', 'Tardanza')], max_length=20)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='face_face.alumno')),
                ('sesion_curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='face_face.sesioncurso')),
            ],
        ),
    ]
