#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-18
# @Author  : Jonathan Zhou
# @Version : 0.0.1
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.

@python_2_unicode_compatible
class Author(models.Model):
    name = models.CharField(max_length=50)
    qq = models.CharField(max_length=10)
    addr = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author)
    content = models.TextField()
    score = models.IntegerField()
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def my_property(self):
        return self.first_name + ' ' + self.last_name

    full_name = property(my_property)
