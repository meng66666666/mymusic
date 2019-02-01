from django.urls import path


from mymusic.views import *
from myuser.views import home
from play.views import play
from ranking.views import rankingView
from search.views import search

app_name = 'mymusic'
urlpatterns = [
    path('index/', index, name='index'),
]
