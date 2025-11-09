from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from server.serializers import RegisterSerializer, LoginSerializer


class RegisterUserAPIView(APIView):
    """
        Class basada en el registro de usuarios
    """
    @staticmethod
    def post(request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            user = User.objects.get(username=serializer.data['username'])
            token = Token.objects.create(user=user)

            return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUserAPIView(APIView):
    """
        Class basada en el login del usuario
    """
    @staticmethod
    def post(request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = get_object_or_404(User, username=serializer.data['username'])

            if not user.check_password(serializer.data['password']):
                return Response({'Error': 'Invalid Password'}, status=status.HTTP_400_BAD_REQUEST)

            token, created = Token.objects.get_or_create(user=user)
            serializer = RegisterSerializer(instance=user)

            return Response({'Token': token.key, 'User': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileUserAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    """
        Class basada en enviar el profile del usuario
    """
    @staticmethod
    def get(request):
        serializer = RegisterSerializer(instance=request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
