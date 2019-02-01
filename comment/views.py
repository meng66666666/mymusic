import time

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from mymusic.models import *


def comment(request,song_id):

    if request.method == 'GET':
        song_info = Songs.objects.filter(song_id=song_id).first()
        # 歌曲不存在抛出404异常
        if not song_info:
            raise Http404
        comment_all = song_info.comment_set.all().order_by('-comment_date')
        song_name = song_info.song_name
        page = int(request.GET.get('page',1))
        paginator = Paginator(comment_all,3)
        try :
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)

        return render(request, 'comment.html', locals())

    elif request.method == 'POST':
        comment_text = request.POST.get('comment','')
        user_id = request.session.get('user_id') # 通过session获取当前用户id
        song_info = Songs.objects.filter(song_id=song_id).first()
        id = song_info.id

        if comment_text and user_id:
            user = User.objects.get(pk=user_id)
            figure_path = user.photo
            # print(figure_path)
            comment = Comment()
            comment.comment_text = comment_text
            comment.praise = 0
            comment.user_id = user_id
            comment.comment_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            comment.songs_id = id
            comment.save()

        # return redirect(reverse('comment',args=(song_id,)))
        return render(request,'comment.html',locals())

