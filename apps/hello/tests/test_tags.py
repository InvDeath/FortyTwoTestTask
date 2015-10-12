from django.test import TestCase
from apps.hello.models import Request
from apps.hello.templatetags.hello_extras import edit_link


class TagsTestCase(TestCase):
    def test_edit_link_tag(self):
        '''
        Test edit_link tag
        '''
        request = Request.objects.create()
        self.assertEqual(
            '<a href="/admin/hello/request/{}">(admin)</a>'.format(request.pk),
            edit_link(request))
