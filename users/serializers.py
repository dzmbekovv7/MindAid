from rest_framework import serializers
from django.core.mail import send_mail
import random
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from posts.serializers import GetSharePostsSerializer, GetHelpPostsSerializer
from .models import MindAidUser
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
User = get_user_model()


class GetUsersSerializer(serializers.ModelSerializer):
    share_posts = GetSharePostsSerializer( many=True, read_only=True)
    help_posts = GetHelpPostsSerializer( many=True, read_only=True)

    class Meta:
        model = MindAidUser
        fields = '__all__'

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
        code = str(random.randint(100000, 999999))

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            avatar=validated_data.get('avatar'),
            verification_code=code,
            is_verified=False
        )

        send_mail(
            subject="Email verification",
            message=f"Your verification code is: {code}",
            from_email="no-reply@yourapp.com",
            recipient_list=[user.email],
        )

        return user

class VerifyEmailSerializer(serializers.Serializer):
    code = serializers.CharField()
    email = serializers.EmailField()

    def validate(self, attrs):
        user = User.objects.filter(email=attrs['email']).first()

        if not user:
            raise serializers.ValidationError("This email is not registered.")
        if user.is_verified:
            raise serializers.ValidationError("Already verified.")
        if user.verification_code != attrs['code']:
            raise serializers.ValidationError("Invalid code.")

        attrs['user'] = user
        return attrs

    def save(self):
        user = self.validated_data['user']
        user.is_verified = True
        user.verification_code = None
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = User.objects.filter(email=data['email']).first()

        if not user:
            raise serializers.ValidationError("Email not registered.")

        user = authenticate(
            username=user.username,  # still username-based auth
            password=data['password']
        )

        if not user:
            raise serializers.ValidationError("Invalid password.")

        if not user.is_verified:
            raise serializers.ValidationError("Email not verified.")

        refresh = RefreshToken.for_user(user)

        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user_id": user.id,
            "email": user.email,
        }

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    new_password2 = serializers.CharField(write_only=True)

    def validate_old_password(self, value):
        user = self.context['request'].user

        if not user.check_password(value):
            raise serializers.ValidationError("Old password is incorrect.")

        return value

    def validate(self, attrs):
        if attrs['new_password'] != attrs['new_password2']:
            raise serializers.ValidationError("Passwords do not match.")
        if attrs['old_password'] == attrs['new_password']:
            raise serializers.ValidationError("Old password is the same as new password.")

        validate_password(attrs['new_password'], self.context['request'].user)

        return attrs

    def save(self, **kwargs):
        user = self.context['request'].user
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user