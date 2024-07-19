from django.db import models
import uuid


class Movie(models.Model):
    uuid = models.UUIDField(unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    genres = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title


class Collection(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    movies = models.ManyToManyField(Movie, related_name='collection')
    user = models.ForeignKey('app_auth.CustomUser', related_name='collections', on_delete=models.CASCADE)

    def __str__(self):
        return self.title