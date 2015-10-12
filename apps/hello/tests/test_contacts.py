import StringIO
import json

from django.test import TestCase, Client
from apps.hello.models import Contacts
from django.core.urlresolvers import reverse


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

    def test_save_data(self):
        '''
        Test update contacts
        '''
        self.client.login(username='admin', password='admin')
        contacts = Contacts.objects.all()[0]
        img_file = StringIO.StringIO(
            'GIF87a\x01\x00\x01\x00\x80\x01\x00\x00\x00\x00ccc,'
            '\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;')

        img_file.name = 'test_img_file.gif'
        data = {
            'bio': 'About me',
            'first_name': 'm',
            'last_name': 'm',
            'jabber': 'invdeath@khavr.com',
            'date_of_birth': '1990-03-03',
            'skype': 'mmospanenko',
            'photo': img_file,
            'other_contacts': 'mmospanenko@gmail.com',
            'email': 'mmospanenko@gmail.com'
        }

        response = self.client.post(
            reverse('contacts_edit', kwargs={'id': contacts.pk}), data=data,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertContains(response, '"OK"')
        contacts = Contacts.objects.all()[0]
        self.assertEqual(contacts.first_name, 'm')

    def test_save_errors(self):
        '''
        Test method returns errors in JSON
        '''
        self.client.login(username='admin', password='admin')
        contacts = Contacts.objects.all()[0]
        data = {
            'bio': '',
            'first_name': '',
            'last_name': '',
            'jabber': '',
            'date_of_birth': '',
            'skype': '',
            'photo': '',
            'other_contacts': '',
            'email': ''
        }
        response = self.client.post(
            reverse('contacts_edit', kwargs={'id': contacts.pk}), data=data,
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.reason_phrase, u'BAD REQUEST')
