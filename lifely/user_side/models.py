from django.db import models
from django.contrib.auth.models import User


class Passwords(models.Model):
    user = models.ForeignKey(
        User, blank=True, null=True,  on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username
