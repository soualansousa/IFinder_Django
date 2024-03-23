from django.db import models
from django.contrib.auth.models import User

class Objeto(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title