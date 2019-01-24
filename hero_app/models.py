from django.db import models

class Hero(models.Model):
    alias = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
