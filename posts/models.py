from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
class SharePost(models.Model):
    FILTERS = [
        (1, "anxiety"),
        (2, "depression"),
        (3, "sadness"),
    ]
    heading = models.CharField(max_length=100)
    text = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="share_posts"
    )
    show_nickname = models.BooleanField(default=False)
    filter = models.IntegerField(choices=FILTERS, default=3)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null =True)

class SharePostComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    share_post = models.ForeignKey(SharePost, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class HelpPost(models.Model):
    FILTERS = [
        (1, "work"),
        (2, "relationship"),
        (3, "friendship"),
        (4, "family")
]
    STATE = [
        (1, "tired"),
        (2, "stress"),
        (3, "sad")

    ]
    heading = models.CharField(max_length=100)
    text = models.TextField()
    show_nickname = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="help_posts"
    )
    filter = models.IntegerField(choices=FILTERS, default=1)
    state = models.IntegerField(choices=STATE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

class HelpPostComment(models.Model):
    help_post= models.ForeignKey(HelpPost, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)