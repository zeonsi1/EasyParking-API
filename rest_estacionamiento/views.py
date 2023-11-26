from django.shortcuts import render
from .serializers import UsurioSerializer
from core.models import Usuario
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
# Create your views here.

class RegistrarView(APIView):
    def post(self, request):
        try:
            data = JSONParser().parse(request)
        
            nombre_usuario = data['nombre_usuario']
            correo_usuario = data['correo_usuario']
            password_usuario = data['pass1']

    
            if Usuario.objects.filter(correo_usuario=correo_usuario).exists():
                return JsonResponse({'error': 'El correo electrónico ya está registrado'}, status=400)

            Usuario.objects.create(
                nombre_usuario=nombre_usuario,
                correo_usuario=correo_usuario,
                password_usuario=password_usuario,
            )

            return JsonResponse({'Mensaje': 'Usuario Registrado'}, status=200)
        except Exception as e:            
            return JsonResponse({'error': 'Error en el registro del usuario', 'detalle': str(e)}, status=500)
    

class UsuarioView(APIView):
    def post(self, request):
        try:
            data = JSONParser().parse(request)
            correo = data['correo_usuario']
            password = data['password']

            usuario = Usuario.objects.get(correo_usuario=correo, password_usuario=password)
            serializer = UsurioSerializer(usuario)
            serialized_data = serializer.data
            return JsonResponse(serialized_data, safe=False)
        except Usuario.DoesNotExist:
            return JsonResponse({'error': 'Credenciales inválidas'}, status=400)
        except Exception as e:            
            return JsonResponse(str(e), status=500)
        