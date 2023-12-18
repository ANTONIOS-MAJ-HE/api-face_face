from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Docente, Curso, Alumno, InscripcionCurso, SesionCurso, Asistencia

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class TokenObtainPairSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError('Invalid username/password.')
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

class DocenteSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Docente
        fields = ['user', 'nombres', 'apellidos', 'dni']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        docente = Docente.objects.create(user=user, **validated_data)
        return docente

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['nombre', 'docente', 'ciclo']

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ['codigo', 'nombre', 'cursos']

class InscripcionCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InscripcionCurso
        fields = ['alumno', 'curso', 'fecha_inscripcion']

class SesionCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SesionCurso
        fields = ['curso', 'fecha', 'tema', 'contenido']

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = ['sesion_curso', 'alumno', 'estado_asistencia']
