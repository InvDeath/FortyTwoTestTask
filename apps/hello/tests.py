from django.test import TestCase, Client


class ContactsTestsCase(TestCase):
    fixtures = ['initial_data.json']

    def setUp(self):
        self.client = Client()

    def test_data(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['email'], 'mmospanenko@gmail.com')
        self.assertEqual(response.context['first_name'], 'Maksym')
        self.assertEqual(response.context['other_contacts'], 'mmospanenko@gmail.com')
        self.assertEqual(response.context['jabber'], 'invdeath@khavr.com')
        self.assertEqual(response.context['skype'], 'mmospanenko')
        self.assertEqual(response.context['date_of_birth'], '1990-03-03')
        self.assertEqual(response.context['bio'], 'About me')
        self.assertEqual(response.context['last_name'], 'Mospanenko')
