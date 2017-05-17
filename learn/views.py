# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    # return HttpResponse(u'Welcome to your first page.')
    return render(request, 'home.html')


def add(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
