from django.db import models


class Track(models.Model):
    file = models.FileField(upload_to='musics/')
    artist = models.CharField(max_length=200)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
