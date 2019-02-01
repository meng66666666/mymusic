from django.contrib import admin

# Register your models here.
from mymusic.models import Label, Singer, Songs

admin.site.register([Label,Singer,Songs])