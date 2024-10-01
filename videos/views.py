from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list_your_videos(request):
    return HttpResponse('Список ваших видео')

def list_recommended_videos(request):
    return HttpResponse('Список рекомендованных видео')

def load_video(request):
    return HttpResponse('Загрузить видео')