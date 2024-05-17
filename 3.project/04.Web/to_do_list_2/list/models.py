from django.db import models

# Create your models here.
class Create(models.Model):
    content = models.CharField(max_length = 25)