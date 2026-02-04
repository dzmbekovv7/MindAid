from django.shortcuts import render
from rest_framework import generics
from .models import MindAidUser
from .serializers import RegisterSerializer, VerifyEmailSerializer, LoginSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = MindAidUser.objects.all()

class VerifyEmailView(generics.CreateAPIView):
    serializer_class = VerifyEmailSerializer
    permission_classes = [AllowAny]

class LoginUser(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)
