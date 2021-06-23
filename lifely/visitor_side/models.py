from django.db import models
# from django.contrib.auth.models import Heading

# Create your models here.


class Aboutus(models.Model):
    heading = models.CharField(max_length=20, null=True)
    date = models.DateField(null=True)
    body = models.TextField(null=True)
    midbody = models.TextField(null=True)
    lastbody = models.TextField(null=True)
