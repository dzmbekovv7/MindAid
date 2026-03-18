from django.db import models
from django.contrib.auth.models import User,AbstractUser

class MindAidUser(AbstractUser):
    ROLES = [
        ('user', 'User'),
        ('admin', 'Admin'),
        ('moderator', 'Moderator'),
    ]
    role = models.CharField(max_length=10, choices=ROLES, default='user')
    show_nickname = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=50, blank=True, null=True)
    last_active = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.username
