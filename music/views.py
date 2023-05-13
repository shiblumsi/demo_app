from django.shortcuts import render,HttpResponse
from .models import Album, Artist, Song, Playlist
from .forms import SongCreateform
# Create your views here.


def home(request):
    album = Album.objects.all()
    artist = Artist.objects.all()
    song = Song.objects.all()
    playlist = Playlist.objects.all()

    context = {
        'album':album,'artist':artist,'song':song,'playlist':playlist
    }

    return render(request,'home.html',context)


def querys(request):
    song = Song.objects.get(id=1)    #obj access MODEL attribute
    song1 = Song.objects.all()        #queryset no access MODEL attribute
    for i in song1:
        print('tttttttttttt',type(i),i) #obj
    print('ggggggggggggg',type(song.album),type(song1))

    songs = Song.objects.filter(album__artist__name='Momtaz').get(id=1) # __ use on queryset

    print('tyyyyyyyyyyyy')
   
    return HttpResponse(songs.album.artist.description) #All queryes for a obj


def get_album_song_by_user(request):
    #album = Album.objects.exclude(artist__user=request.user)   #return query ser without artist__user=request.user 
    album = Album.objects.filter(artist__user=request.user)
    #album = Album.objects.filter(singer__user=request.user)
    #songs = Song.objects.select_related('album').all()   # reduse query
    songs = Song.objects.all()
    #so = album.song_set.all()
    #print('444444444444444444')

    return render(request, 'get_album_by_user.html', {'album':album,'songs':songs})

def song_create(request,pk):
    album = Album.objects.get(id=pk)
    songs = album.song_set.all()   #songs under a album object; usecase of _set.all()
    artist = Artist.objects.get(user=request.user)
   
    if request.method == 'POST':
        form = SongCreateform(request.POST,request.FILES)
        if form.is_valid():
            song = form.save(commit=False)
            song.album = album
            song.artist = Artist.objects.get(user=request.user)
            song.save()
    else:
        form = SongCreateform()
    return render(request, 'song_create.html',{'form':form,'songs':songs})

def playlist(request):
    playlists = Playlist.objects.get(id=1)
    print('pppppppppppppppppp',playlists.songs_set.all())
    return render(request,'playlist.html',{'playlists':playlists}) 