from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Image(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200)
    user_tags = models.CharField(max_length=200, null=True, blank=True)
    auto_tags = models.CharField(max_length=200, null=True, blank=True)
    time_stamp = models.DateTimeField(default=timezone.now)
    file = models.ImageField(upload_to="uploads/images")
    is_public = models.BooleanField(default=True)

    class Meta:
        db_table = "images"

    @property
    def tags(self):
        return f"{self.auto_tags if self.auto_tags else ''} {self.user_tags if self.user_tags else ''}".strip().split()[:10]

    def __str__(self):
        return self.title
