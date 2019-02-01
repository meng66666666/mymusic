from django.urls import path

from label.views import label

app_name = 'label'
urlpatterns = [
    path('label/',label,name='label'),
]