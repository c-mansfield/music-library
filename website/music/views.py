from django.http import Http404
from django.shortcuts import render,get_object_or_404

from .models import Album, Song

# Create your views here.
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