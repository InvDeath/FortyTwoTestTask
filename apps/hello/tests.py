from django.test import TestCase, Client
import datetime


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
