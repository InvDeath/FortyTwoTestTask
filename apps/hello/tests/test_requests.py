from django.test import TestCase, Client
from apps.hello.models import Request
from django.core.serializers import deserialize
from django.utils import timezone


class RequestsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_request_writes(self):
        '''
        Test middleware request save
        '''
        self.assertEqual(Request.objects.all().count(), 0)
        self.client.get('/')
        self.assertEqual(Request.objects.all().count(), 1)

    def test_requests_page(self):
        '''
        Test list of last requests
        '''
        self.client.get('/')
        response = self.client.get('/requests/')
        self.assertEqual(response.context['requests'].count(), 2)

    def test_ajax_update(self):
        '''
        Return last new requests
        '''
        self.client.get('/')
        response = self.client.get('/requests/',
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.reason_phrase, 'OK')

    def test_ten_requests(self):
        '''
        Test return only 10 requests
        '''
        for i in range(15):
            Request.objects.get_or_create(
                time=timezone.now() + timezone.timedelta(hours=i))
        response = self.client.get('/requests/',
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        requests = list(deserialize("json", response._container[0]))
        self.assertEqual(len(requests), 10)
        response = self.client.get('/requests/')
        self.assertEqual(len(response.context['requests']), 10)
        # only latest requests?
        newest_from_reminds = Request.objects \
            .exclude(pk__in=[r.pk for r in response.context['requests']]) \
            .latest('time')
        for rec in response.context['requests']:
            self.assertLess(newest_from_reminds.time, rec.time)
