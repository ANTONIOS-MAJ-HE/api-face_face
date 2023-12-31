from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Docente, Curso, Asistencia, SesionCurso, Alumno, InscripcionCurso
from .serializers import AlumnoSerializer, AsistenciaSerializer, CursoSerializer, DocenteSerializer, SesionCursoSerializer, UserSerializer, TokenObtainPairSerializer, UserRegistrationSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = TokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class InscripcionCursoViewSet(viewsets.ModelViewSet):
    queryset = InscripcionCurso.objects.all()
    serializer_class = InscripcionCurso

class SesionCursoViewSet(viewsets.ModelViewSet):
    queryset = SesionCurso.objects.all()
    serializer_class = SesionCursoSerializer

class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Successfully registered a new user."
            data['username'] = account.username
            data['email'] = account.email
        else:
            data = serializer.errors
        return Response(data, status=status.HTTP_201_CREATED if serializer.is_valid() else status.HTTP_400_BAD_REQUEST)
