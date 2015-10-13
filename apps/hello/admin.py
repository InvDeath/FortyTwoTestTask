from django.contrib import admin
from apps.hello.models import Contacts, Request, Action

admin.site.register(Contacts)
admin.site.register(Request)
admin.site.register(Action)
