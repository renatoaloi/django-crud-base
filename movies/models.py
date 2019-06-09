from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255)
    synopsis = models.TextField()
    actors = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    duration = models.IntegerField()
    rate = models.IntegerField()
