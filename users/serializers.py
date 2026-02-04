from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.mail import send_mail
import random
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import MindAidUser


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    avatar = serializers.ImageField(required=False)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value

    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        username = validated_data['username']
        avatar = validated_data.get('avatar', None)

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        code = str(random.randint(100000, 999999))
        profile = MindAidUser.objects.create(
            user=user,
            email=email,
            username=username,
            avatar=avatar,
            verification_code=code,
        )

        send_mail(
            subject="Email verification",
            message=f"Your verification code is: {code}",
            from_email="no-reply@yourapp.com",
            recipient_list=[user.email],
        )

        return profile

class VerifyEmailSerializer(serializers.Serializer):
    code = serializers.CharField()
    email = serializers.EmailField()

    def validate(self, attrs):
        email = attrs.get('email')
        code = attrs.get('code')
        user = MindAidUser.objects.filter(email=email).first()
        if not user:
            raise serializers.ValidationError("This email is not registered.")
        if user.is_verified:
            raise serializers.ValidationError("This email is already verified.")
        if user.verification_code != code:
            raise serializers.ValidationError("This code is invalid.")
        attrs['user'] = user
        return attrs

    def save(self, **kwargs):
        user =self.validated_data['user']
        user.is_verified = True
        user.verification_code = None
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        try:
            user_obj = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            raise serializers.ValidationError("This email is not registered.")

        user = authenticate(
            username=user_obj.username,
            password=data['password']
        )

        if not user:
            raise serializers.ValidationError("Invalid password.")

        profile = MindAidUser.objects.get(user=user)
        if not profile.is_verified:
            raise serializers.ValidationError("This email is not verified.")

        refresh = RefreshToken.for_user(user)

        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user_id": user.id,
            "email": user.email,
        }
