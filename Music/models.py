from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100)
    actors = models.TextField()
    director = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=50)
    singer = models.CharField(max_length=200)
    music_director = models.CharField(max_length=50)
    movie = models.ForeignKey(to=Movie, on_delete=models.CASCADE, related_name="movies")

    def __str__(self):
        return self.name

