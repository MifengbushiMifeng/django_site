# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


# Create your views here.

def index(request):
    # return HttpResponse(u'Welcome to your first page.')
    content_str = u'Learning Django and building my first django web site.'
    tutoriallist = ['Python', 'Django', 'Jinja']
    info_dict = {'site': u'My First Django Site', 'content': u'Stay Hungary'}

    list = map(str, range(100))

    return render(request, 'home.html', {'contentstr': content_str,
                                         'tutorialList': tutoriallist, 'info_dict': info_dict,
                                         'list': list})


def add(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def old_add_redirect(request, a, b):
    # return HttpResponseRedirect(
    #     reverse('add2', args=(a, b))
    # )
    return HttpResponseRedirect(reverse('add', args=(a, b)))
