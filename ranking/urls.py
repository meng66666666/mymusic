from django.contrib import admin
from django.urls import path, include

from mymusic.views import index
from play.views import play
from ranking.views import rankingView
from search.views import search
from user.views import user_home, logout

app_name = 'ranking'
urlpatterns = [
    path('ranking/', rankingView, name='ranking'),
    path('home/', user_home, name='home'),
    path('logout/', logout, name='logout'),
]
