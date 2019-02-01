from django.shortcuts import render

# Create your views here.
from mymusic.models import Label, Songs


def label(request):
    label_list = Label.objects.all()
    for lis in label_list:
        song_info = Songs.objects.filter(label_id=lis.id)
    return render(request,'label.html',locals())