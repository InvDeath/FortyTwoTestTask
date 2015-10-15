from django.test import TestCase, Client
from apps.hello.models import Request
from django.core.serializers import deserialize
from django.core.urlresolvers import reverse


class RequestsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_request_writes(self):
        '''
        Test middleware request save
        '''
        self.assertEqual(Request.objects.all().count(), 0)
        Request.objects.create()
        self.assertEqual(Request.objects.all().count(), 1)

    def test_requests_page(self):
        '''
        Test list of last requests
        '''
        Request.objects.create()
        response = self.client.get(reverse('requests'))
        self.assertEqual(response.context['requests'].count(), 2)

    def test_ajax_update(self):
        '''
        Return last new requests
        '''
        Request.objects.create()
        response = self.client.get(reverse('requests'),
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.reason_phrase, 'OK')

    def test_ten_requests(self):
        '''
        Test return only 10 requests
        '''
        for i in range(15):
            Request.objects.create()
        response = self.client.get(reverse('requests'),
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        requests = list(deserialize("json", response._container[0]))
        self.assertEqual(len(requests), 10)
        response = self.client.get(reverse('requests'))
        self.assertEqual(len(response.context['requests']), 10)
        # only latest requests?
        latest_ten = Request.objects.order_by('-time')[:10]
        self.assertEqual(set(latest_ten), set(response.context['requests']))

    def test_by_priority(self):
        '''
        Test request by priority
        '''
        for i in range(15):
            Request.objects.create(priority=i)
        response = self.client.get(reverse('requests'))
        highest_ten = Request.objects.order_by('-priority')[:10]
        self.assertEqual(set(highest_ten), set(response.context['requests']))
