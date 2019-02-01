from django.shortcuts import render

from mymusic.models import Songs


def rankingView(request):
    search_song = Songs.objects.values('song_name')
    All_list = Songs.objects.all().order_by('-play_num').order_by('-download_num')[20:35]
    song_info = Songs.objects.all().order_by('-download_num').order_by('-play_num')[0:10]
    return render(request,'ranking.html',locals())

