from django.shortcuts import render
from apps.hello.models import Contacts
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    try:
        contacts = Contacts.objects.get()
    except ObjectDoesNotExist:
        contacts = None
    return render(request, 'hello/home.html', {'contacts': contacts})
