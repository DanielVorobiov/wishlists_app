from rest_framework import serializers

from user.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name','last_name','email']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')

    


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
