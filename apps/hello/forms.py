from django import forms
from apps.hello.models import Contacts


class ConractsForm(forms.ModelForm):
    class Meta:
        model = Contacts
