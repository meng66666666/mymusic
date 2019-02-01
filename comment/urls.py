from django.urls import path, include

from comment.views import comment
from mymusic.views import index
from myuser.views import home
from play.views import play
from ranking.views import rankingView
from search.views import search
from user.views import user_home, logout

urlpatterns = [

    path('/comment/<song_id>/',comment,name='comment'),

    path('home/', home, name='home'),
    path('ranking/',rankingView,name='ranking'),
    path('home/',user_home,name='home'),
    path('logout/', logout, name='logout'),
    path('index/', index, name='index'),
    path('play/<song_id>/', play, name='play'),
    path('search/',search, name='search'),
]