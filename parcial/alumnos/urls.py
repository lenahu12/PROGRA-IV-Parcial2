from django.urls import path
from .views import DashboardView, AlumnoCreateView, enviar_pdf

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('nuevo/', AlumnoCreateView.as_view(), name='nuevo_alumno'),
    path('<int:pk>/enviar-pdf/', enviar_pdf, name='enviar_pdf'),
]