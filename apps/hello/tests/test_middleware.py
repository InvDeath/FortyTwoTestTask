from django.test import TestCase
from apps.hello.models import Request


class MiddlewareTestCase(TestCase):
    def test_save_request(self):
        '''
        Test save request
        '''
        self.assertEqual(Request.objects.all().count(), 0)
        Request.objects.create()
        self.assertEqual(Request.objects.all().count(), 1)
        self.client.get('/requests/',
                        HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(Request.objects.all().count(), 1)
