import hashlib
import os
import re
import uuid

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from Music import settings
from mymusic.models import User
from myuser.forms import UserRegister


def take_md5(content):
    md5 = hashlib.md5()  # 创建hash加密实例
    md5.update(content.encode())  # hash加密
    result = md5.hexdigest()  # 得到加密结果
    return result


def home(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(pk=user_id)
    return render(request, 'home.html', locals())


def register(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            name_filter = User.objects.filter(username=username)

            if len(name_filter) > 0:
                return render(request, 'register.html', {'error': '用户名已存在'})
            else:
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']

                if password1 != password2:
                    return render(request, 'register.html', {'error': '密码不一致！'})
                else:
                    password = take_md5(password1)
                    phone_num = form.cleaned_data['phone_num']
                    # print(type(phone_num))
                    rp = re.compile('(^[1][3-5|7-8][0-9]{9}$)')
                    if not rp.match(phone_num):
                        return render(request, 'register.html', {'error': '手机号码错误！'})
                    else:
                        photo = request.POST.get('photo')
                        user = User.objects.create(username=username, password=password, phone_num=phone_num,
                                                   photo=photo)
                        return redirect(reverse('myuser:login'))

    if request.method == 'GET':
        form = UserRegister()
        return render(request, 'register.html', locals())


@csrf_exempt  # 不会经过中间件
def upload(request):
    photoFile = request.FILES.get('photo')
    # 将上传的文件保存到/static/images/tmp目录中
    dir_ = os.path.join(settings.BASE_DIR, 'static/images/tmp')
    file_name = uuid.uuid4().hex + ('.jpg' if photoFile.content_type.endswith('jpeg') else '.png')
    with open(os.path.join(dir_, file_name), 'wb') as f:
        for chunk in photoFile.chunks():
            f.write(chunk)
    return JsonResponse({'msg': 1,
                         'path': f'images/tmp/{file_name}'})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html', locals())

    if request.method == 'POST':
        username = request.POST.get('loginUser')
        password = request.POST.get('password')
        password1 = take_md5(password)
        # print(password1)
        users = User.objects.filter(username=username, password=password1)

        if users:
            user = users.first()
            request.session['user_id'] = user.id
            return redirect(reverse('user:home'))
        else:
            return render(request, 'login.html', {'error': '用户名或密码错误!'})
