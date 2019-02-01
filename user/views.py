import os
import uuid

from django.shortcuts import render, redirect
from django.urls import reverse

from Music import settings
from myuser.views import upload

from mymusic.models import User


def user_home(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(pk=user_id)
        username = user.username
        figure_path = user.photo
        # print(figure_path)
    else:
        username = "点击登录"

    page = 1
    return render(request, 'home.html', locals())


def logout(request):
    request.session.flush()
    return redirect(reverse('mymusic:index'))
