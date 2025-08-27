from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mod(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='mods/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
