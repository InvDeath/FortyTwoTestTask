from django.contrib import admin
from apps.hello.models import Contacts, Request

admin.site.register(Contacts)
admin.site.register(Request)
