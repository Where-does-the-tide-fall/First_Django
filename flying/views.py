from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def fly_views(request):
    return HttpResponse('<h1> ni yao de ai</h1>')
