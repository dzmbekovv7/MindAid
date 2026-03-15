from django.db import models
from django.contrib.auth.models import User

class SharePost(models.Model):
    FILTERS = [
        (1, "anxiety"),
        (2, "depression"),
        (3, "sadness"),
    ]
    heading = models.CharField(max_length=100)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    show_nickname = models.BooleanField(default=False)
    filter = models.IntegerField(choices=FILTERS, default=3)

class SharePostComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    share_post = models.ForeignKey(SharePost, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
