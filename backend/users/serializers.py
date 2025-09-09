from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    """
    Serializador para criar um novo usuário.
    Inclui validação de confirmação de senha.
    """
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password_confirmation', 'bio', 'avatar']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        """
        Valida se a senha e a confirmação de senha coincidem.
        """
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError(
                {"password_confirmation": "As senhas não coincidem."}
            )
        return data

    def create(self, validated_data):
        """
        Remove o campo password_confirmation e cria o usuário com a senha hashada.
        """
        validated_data.pop('password_confirmation')  # Remove a confirmação antes de criar
        return User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            avatar=validated_data.get('avatar', None)
        )


class UserSerializer(serializers.ModelSerializer):
    """
    Serializador para listar ou detalhar informações de um usuário.
    """
    class Meta:
        model = User
        fields = ['id', 'email', 'bio', 'avatar']


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'username'

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'), username=username, password=password)
            if not user:
                raise AuthenticationFailed(_('Usuário ou senha incorretos'), code='authorization')
        else:
            raise AuthenticationFailed(_('Username e senha são obrigatórios'), code='authorization')

        refresh = self.get_token(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': UserSerializer(user).data
        }

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Você pode adicionar informações extras ao token, se desejar:
        token['email'] = user.email
        return token
