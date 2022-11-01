from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('This is a main list')


def group_posts(request,slug):
    return HttpResponse(f'You are on the page{slug}')