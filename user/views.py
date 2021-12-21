from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import decorators, response, status, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from user.models import User
from user import serializers

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


@decorators.api_view(['POST'])
@decorators.authentication_classes([BasicAuthentication])
@decorators.permission_classes([permissions.AllowAny])
def register(request):
    serializer = serializers.RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = User(
        email = serializer.validated_data['email'], 
        password = serializer.validated_data['password'],
        first_name = serializer.validated_data['first_name'],
        last_name = serializer.validated_data['last_name'])
    user.set_password(serializer.validated_data['password'])
    user.save()
    data = {"message": "User registered successfully."}
    return response.Response(data, status=status.HTTP_200_OK)


@decorators.api_view(['POST'])
@decorators.authentication_classes([BasicAuthentication])
@decorators.permission_classes([permissions.AllowAny])
def login(request, format=None):
    serializer = serializers.LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    try:
        user = User.objects.get(email=serializer.data['email'])
        if not user.check_password(serializer.data['password']):
            error = {"error": "Wrong password."}
            return response.Response(error, status.HTTP_400_BAD_REQUEST)

    except User.DoesNotExist:
        error = {"error": "User does not exist."}
        return response.Response(error, status=status.HTTP_404_NOT_FOUND)


    data = {
        "message": "Login successful.",
    }
    return response.Response(data)
   