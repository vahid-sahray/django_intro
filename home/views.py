from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


def home(request):
    return HttpResponse('Hello baby...')

