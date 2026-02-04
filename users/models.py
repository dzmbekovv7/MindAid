from django.db import models
from django.contrib.auth.models import User

class MindAidUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    show_nickname = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=50, blank=True, null=True)
    last_active = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.username
