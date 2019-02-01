from django.shortcuts import render,redirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Q

from mymusic.models import Songs


def search(request,page):
    if request.method == 'GET':

        kword = request.GET.get('kword', '')
        # print(kword, 22222222222)
        if kword:
            song_info = Songs.objects.values('song_id','song_name', 'singer__singer_name', 'song_time').filter(
                Q(song_name__icontains=kword) | Q(singer__singer_name__icontains=kword)).order_by('-play_num').all()

        else:
            song_info = Songs.objects.values('song_id','song_name', 'singer__singer_name', 'song_time').order_by(
                '-play_num').all()[:30]
        # 分页
        paginator = Paginator(song_info, 5)
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)


    elif request.method == 'POST':

        kword  = request.POST.get('kword','')
        # request.session['kword'] = kword
        # print(kword,333333333333333)
        if kword:
            song_info = Songs.objects.values('song_id','song_name', 'singer__singer_name', 'song_time').filter(
                Q(song_name__icontains=kword) | Q(singer__singer_name__icontains=kword)).order_by('-play_num').all()

        else:
            song_info = Songs.objects.values('song_name', 'singer__singer_name', 'song_time').order_by('-play_num').all()[:30]
        # 分页
        paginator = Paginator(song_info,5)
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)  # 返回总的页数

        # return redirect('search:search', contacts.number,locals())
        # return render(request,'label.html',locals())

    return render(request, 'search.html', locals())