from django.http import Http404
from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Album, Song

# Create your views here.
"""
def index(request):
    all_albums = Album.objects.all()
    #template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums,
    }

    return render(request, 'music/index.html', context)

def details(request, album_id):
    #try:
    #    album = Album.objects.get(id=album_id)
    #except Album.DoesNotExist:
    #    raise Http404("Album does not exist")
    album = get_object_or_404(Album, id=album_id)

    return render(request, 'music/detail.html', {'album': album})

def favourite(request, album_id):
    album = get_object_or_404(Album, id=album_id)

    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "You did not select a valid song"
        })
    else:
        selected_song.is_favourite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})
"""

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailsView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_art']