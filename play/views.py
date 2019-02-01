from django.shortcuts import render

# Create your views here.
from mymusic.models import Songs, Singer


def play(request,song_id):
    song = Songs.objects.get(song_id=song_id)
    current_name=song.singer.singer_name
    play_list = Songs.objects.all()
    singer=Singer.objects.get(singer_name=current_name)
    song_relevant=singer.songs_set.all()

    return render(request,'play.html',locals())