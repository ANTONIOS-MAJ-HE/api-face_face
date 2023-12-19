from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from face_face import views
from .views import UserRegistrationView
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'docentes', views.DocenteViewSet)
router.register(r'cursos', views.CursoViewSet)
router.register(r'alumno', views.AlumnoViewSet)
router.register(r'InscripcionCurso', views.InscripcionCursoViewSet)
router.register(r'SesionCurso', views.SesionCursoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/custom-login/', views.UserViewSet.as_view({'post': 'login'})), # Ruta para el login personalizado
    path('api/register/', UserRegistrationView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
