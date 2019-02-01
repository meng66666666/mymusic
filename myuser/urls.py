from django.urls import path

from myuser.views import *

app_name = 'myuser'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('upload/',upload,name='upload'),
]
