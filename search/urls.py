from django.urls import path

from play.views import play
from ranking.views import rankingView
from search.views import search

app_name = 'search'

urlpatterns = [
    path('search/<int:page>/',search,name='search'),
]