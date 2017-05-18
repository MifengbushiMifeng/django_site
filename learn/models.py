# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.

# class Users(models.Model):
#     id = models.CharField(max_length=50)
#     email = models.EmailField(max_length=50)
#     password = models.CharField(max_length=50)
#     admin = models.CharField(max_length=1)
#     name = models.CharField(max_length=50)
#     image = models.CharField(max_length=500)

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __unicode__(self):
        return self.name


if __name__ == '__main__':
    print 'run main method'
    Person.objects.create(name='Jonathan', age=28)
