from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Главная страница сайта Мир Книг Селивановой')

# Create your views here.
