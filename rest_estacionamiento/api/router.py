from django.urls import path
from rest_estacionamiento.views import RegistrarView, UsuarioView

urlpatterns = [
    path('registro', RegistrarView.as_view()),
    path('login', UsuarioView.as_view()),
]