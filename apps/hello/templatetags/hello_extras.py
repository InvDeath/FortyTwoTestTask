from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag
def edit_link(obj):
    url = reverse(
        'admin:{}_{}_change'.format(obj._meta.app_label, obj._meta.model_name),
        args=(obj.pk,))
    return '<a href="{}">(admin)</a>'.format(url)
