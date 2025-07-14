from rest_framework import serializers
from django.contrib.auth import get_user_model
from users.models import Perfil



User = get_user_model()

class PerfilSerializer(serializers.ModelSerializer):
    rol = serializers.ChoiceField(choices=Perfil.ROLES, required=False)
    class Meta:
        model = Perfil
        fields = ['perfil_id', 'dni', 'telefono', 'direccion', 'rol']

class UserSerializer(serializers.ModelSerializer):
    perfil = PerfilSerializer(many=False, required=True)

    class Meta:
        model = User
        #El password solo esta disponible para escritura
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'perfil']
        #oculta la contraseña en las respuestas
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
    def create(self, validated_data):
        #Extrae los datos del Perfil si estan disponibles
        perfil_data = validated_data.pop('perfil', None)
        #Extrae la contraseña para usar el hashing
        password = validated_data.pop('password', None)
        #Crear el usuario
        user = User.objects.create_user(password=password, **validated_data)
            
        #crea o actualiza el perfil si existen los datos 
        if perfil_data:
            perfil = user.perfil

            for attr, value in perfil_data.items():
                #funcion para modificar dinamicamente los atributos de un objeto
                setattr(perfil, attr, value)
            perfil.save()

            return user
        
    def update(self,instance, validated_data):
        perfil_data = validated_data.pop('perfil', None)

        for attr, value in perfil_data.items():
            if attr == 'password':
                #set_password() para hashear la contraseña nueva
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        
        instance.save()

        if perfil_data:
            perfil = getattr(instance, 'perfil', None)

            if perfil:
                for attr, value in perfil.items():
                    setattr(perfil, attr, value)
                perfil.save()
            else:
                Perfil.objects.create(user=instance, **perfil_data)

        return instance