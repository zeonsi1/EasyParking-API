from rest_framework import serializers
from core.models import Usuario

class UsurioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        safe = False
