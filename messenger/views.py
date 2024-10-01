from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def messages(request):
    return HttpResponse('Ваши сообщения')

def create_group(request):
    return HttpResponse('Создать беседу')

def write_friend(request):
    return HttpResponse('Написать другу')

