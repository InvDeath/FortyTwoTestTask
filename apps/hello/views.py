import json

from django.core.serializers import serialize
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect
from apps.hello.models import Contacts, Request
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from apps.hello.forms import ContactsForm
from django.conf import settings


def contacts(request):
    try:
        contacts = Contacts.objects.all()[0]
    except (ObjectDoesNotExist, IndexError):
        contacts = None
    return render(request, 'hello/contacts.html', {'contacts': contacts})


def requests(request):
    request_set = Request.objects.order_by('-priority', '-time')[:10]
    if request.is_ajax():
        return HttpResponse(serialize("json", request_set),
                            content_type="application/json")
    return render(request, 'hello/requests.html', {'requests': request_set})


@login_required(login_url='/admin/')
def contacts_edit(request, id):
    contacts = Contacts.objects.get(pk=id)
    if request.POST:
        form = ContactsForm(request.POST, request.FILES, instance=contacts)
        if form.is_valid():
            form.save()
            if request.is_ajax():
                result = {
                    'status': 'OK',
                    'photo': '{}{}'.format(settings.MEDIA_URL,
                                           contacts.photo.name),
                }
                return HttpResponse(json.dumps(result))
            return redirect('home')
        else:
            if request.is_ajax():
                # Prepare JSON for parsing
                errors_dict = {}
                if form.errors:
                    for error in form.errors:
                        e = form.errors[error]
                        errors_dict[error] = e
                return HttpResponseBadRequest(json.dumps(errors_dict))

    else:
        form = ContactsForm(instance=contacts)
    return render(request, 'hello/contacts_edit.html', {'form': form})
