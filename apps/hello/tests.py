from django.test import TestCase, Client
import datetime
from apps.hello.models import Request


class ContactsTestsCase(TestCase):
    fixtures = ['initial_data.json']

    def setUp(self):
        self.client = Client()

    def test_data(self):
        '''
        test all context data for main page
        '''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['contacts'].email,
                         'mmospanenko@gmail.com')
        self.assertEqual(response.context['contacts'].first_name,
                         'Maksym')
        self.assertEqual(response.context['contacts'].other_contacts,
                         'mmospanenko@gmail.com')
        self.assertEqual(response.context['contacts'].jabber,
                         'invdeath@khavr.com')
        self.assertEqual(response.context['contacts'].skype,
                         'mmospanenko')
        self.assertEqual(response.context['contacts'].date_of_birth,
                         datetime.date(1990, 3, 3))
        self.assertEqual(response.context['contacts'].bio,
                         'About me')
        self.assertEqual(response.context['contacts'].last_name,
                         'Mospanenko')


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
