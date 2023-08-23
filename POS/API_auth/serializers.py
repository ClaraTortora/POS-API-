from rest_framework import serializers 

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}} #Esto se hace para que no se vea la contraseña
        
    def create(self,validated_data):
        user = User(
        email=validated_data['email'],
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name'],
        username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save() #esto se hace para encriptar la contraseña o lo que se quiera ocultar
        return user