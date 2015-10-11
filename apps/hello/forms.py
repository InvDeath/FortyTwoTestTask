from django import forms
from apps.hello.models import Contacts
from django.forms.widgets import FileInput
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminDateWidget


class EditPhotoFileInput(FileInput):
    def render(self, name, value, attrs=None):
        template = '%(input)s'
        data = {'input': None, 'url': None, 'id': None}
        data['id'] = 'id_img_{}'.format(name)
        data['input'] = super(EditPhotoFileInput, self).render(name, value,
                                                               attrs)
        if hasattr(value, 'url'):
            data['url'] = conditional_escape(value.url)
            template = '%(input)s <br><br><img id="%(id)s" src="%(url)s">'
        return mark_safe(template % data)


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts

    photo = forms.ImageField(widget=EditPhotoFileInput())
    date_of_birth = forms.DateField(widget=AdminDateWidget)
