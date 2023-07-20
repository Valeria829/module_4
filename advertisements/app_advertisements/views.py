from django.shortcuts import render
from django.http import HttpResponse


def index(response):
    return HttpResponse('Домашка по 4 занятию.')

def top_sellers(request):
    return render(request, 'top-sellers.html')
