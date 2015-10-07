from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render
from apps.hello.models import Contacts, Request
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    try:
        contacts = Contacts.objects.get()
    except ObjectDoesNotExist:
        contacts = None
    return render(request, 'hello/home.html', {'contacts': contacts})


def requests(request):
    requests = Request.objects.all()[:10]
    if request.is_ajax():
        return HttpResponse(serialize("json", requests), content_type="application/json")
    return render(request, 'hello/requests.html', {'requests': requests})
