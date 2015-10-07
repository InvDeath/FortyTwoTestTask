# -*- coding: utf-8 -*-
from django.db import models


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
