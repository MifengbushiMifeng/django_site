# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Article, Author, Person


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'score')


class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Author)
