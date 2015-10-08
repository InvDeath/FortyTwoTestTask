from django.test import TestCase, Client
from apps.hello.models import Contacts


class ContactsTestsCase(TestCase):
    fixtures = ['initial_data.json']

    def setUp(self):
        self.client = Client()

    def test_data(self):
        '''
        Test all context data for main page
        '''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['contacts'],
                         Contacts.objects.all()[0])

    def test_plural_contacts(self):
        '''
        Test if db contains more then one Contact row
        '''
        second_contact = Contacts(
            first_name='fn',
            jabber='jb',
            bio='bio',
            other_contacts='oc',
            last_name='ln',
            skype='s',
            email='e',
            date_of_birth='1990-03-03'
        )
        second_contact.save()

        response = self.client.get('/')
        self.assertEqual(response.context['contacts'].first_name, 'Maksym')

    def test_rendered_content(self):
        '''
        Test rendered content
        '''
        response = self.client.get('/')
        self.assertContains(response, 'Maksym')
        self.assertContains(response, 'invdeath@khavr.com')
        self.assertContains(response, 'About me')
        self.assertContains(response, 'mmospanenko@gmail.com')
        self.assertContains(response, 'Mospanenko')
        self.assertContains(response, 'mmospanenko')
        self.assertContains(response, 'mmospanenko@gmail.com')
        self.assertContains(response, 'March 3, 1990')

    def test_absent_contact(self):
        '''
        Test if db (contact) empty
        '''
        Contacts.objects.all()[0].delete()
        response = self.client.get('/')
        self.assertContains(response, 'Nothing to show!')
