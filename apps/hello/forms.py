from django import forms
from apps.hello.models import Contacts
from apps.hello.widgets import EditPhotoFileInput
from django.contrib.admin.widgets import AdminDateWidget


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts

    photo = forms.ImageField(widget=EditPhotoFileInput())
    date_of_birth = forms.DateField(widget=AdminDateWidget)
