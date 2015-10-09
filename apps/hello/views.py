from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render
from apps.hello.models import Contacts, Request
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from apps.hello.forms import ConractsForm

def home(request):
    try:
        contacts = Contacts.objects.all()[0]
    except (ObjectDoesNotExist, IndexError):
        contacts = None
    return render(request, 'hello/home.html', {'contacts': contacts})


def requests(request):
    request_set = Request.objects.all()[:10]
    if request.is_ajax():
        return HttpResponse(serialize("json", request_set),
                            content_type="application/json")
    return render(request, 'hello/requests.html', {'requests': request_set})


@login_required
def contacts_edit(request, id):
    contacts = Contacts.objects.get(pk=id)
    form = ConractsForm(instance=contacts)
    return render(request, 'hello/contacts_edit.html', {'form': form})
