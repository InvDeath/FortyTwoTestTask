# -*- coding: utf-8 -*-
from django.db import models
from django_resized import ResizedImageField


class Contacts(models.Model):
    def __unicode__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    bio = models.TextField()
    email = models.EmailField()
    jabber = models.EmailField()
    skype = models.CharField(max_length=100)
    other_contacts = models.TextField(null=True)
    photo = ResizedImageField(upload_to='photos', null=True, size=[200, 200])

    class Meta:
        ordering = ['pk']


class Request(models.Model):
    def __unicode__(self):
        return self.title

    title = models.CharField(max_length=100, default='HTTP request')
    time = models.DateTimeField(auto_now_add=True)
    request = models.TextField()
    priority = models.IntegerField(default=1,
                                   choices=[(i, i) for i in range(1, 11)],
                                   blank=True)

    class Meta:
        ordering = ['-time']


class Action(models.Model):
    def __unicode__(self):
        return self.model

    model = models.CharField(max_length=100)
    instance = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=100)
