from django.db import models

# Create your models here.

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True, db_column='id_usuario')
    nombre_usuario = models.CharField(max_length=25, null=False)
    correo_usuario = models.EmailField(unique=True, max_length=50, null=False)
    password_usuario = models.CharField(max_length=25, null=False)
    telefono_usuario = models.CharField(max_length=12, null=True, blank=True)



