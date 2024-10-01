from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list_friends(request):
    return HttpResponse('Ваши друзья')

def list_best_friends(request):
    return HttpResponse('Ваши лучшие друзья')

def list_recommended_friends(request):
    return HttpResponse('Ваши рекомендованные друзья')
