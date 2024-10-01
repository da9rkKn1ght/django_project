from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list_friends(request):
    return HttpResponse('Список ваших друзей')

def list_best_friends(request):
    return HttpResponse('Список лучших друзей')

def list_recommended_friends(request):
    return HttpResponse('Список рекомендованных друзей')
