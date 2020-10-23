from django.db import models
from django.urls import reverse

# Create your models here.
# All Models get primary key auto

class Album(models.Model):
    artist = models.CharField(max_length=255)    #String row
    album_title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    album_art = models.CharField(max_length=1000)

    # On create new this is redirect url, passing through pk of that object
    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    #Object return string
    def __str__(self):
        return self.artist + ' - ' + self.album_title

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)      #Child table of album, id of album
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=255)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title