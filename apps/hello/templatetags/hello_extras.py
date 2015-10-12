from django import template

register = template.Library()


@register.simple_tag
def edit_link(obj):
    return '<a href="/admin/{}/{}/{}">(admin)</a>'.format(obj._meta.app_label,
                                                          obj._meta.model_name,
                                                          obj.pk)
