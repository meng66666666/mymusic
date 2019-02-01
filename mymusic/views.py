from django.shortcuts import render

from mymusic.models import *


def index(request):
    # 搜索显示前6条
    search_song = Songs.objects.all()
    # 音乐分类
    label_list = Label.objects.all()
    # 热门歌曲(用播放量和下载量排行显示前10条)
    play_hot_song = Songs.objects.order_by('-play_num').order_by('-download_num').all()[:10]
    # 新歌推荐(用发布时间排名前6条)
    daily_recommendation = Songs.objects.order_by('play_num').all()[:6]
    # 排行(按播放量排序)
    search_ranking = search_song[:6]
    down_ranking = Songs.objects.order_by('download_num').all()[:6]
    all_ranking = [search_ranking, down_ranking]
    return render(request, 'index.html', locals())


