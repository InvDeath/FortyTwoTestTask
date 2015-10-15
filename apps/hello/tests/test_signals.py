from django.test import TestCase
from apps.hello.models import Request, Action


class SignalsTestCase(TestCase):
    def test_write_signal(self):
        '''
        Test save, update, delete signals
        '''
        self.assertEqual(Action.objects.filter(model='hello.request').count(),
                         0)
        request = Request.objects.create()
        self.assertEqual(Action.objects.filter(model='hello.request').count(),
                         1)
        self.assertEqual(
            Action.objects.filter(model='hello.request')[0].action,
            'save')
        request.title = 'new title'
        request.save()
        self.assertEqual(Action.objects.filter(model='hello.request',
                                               action='update').count(),
                         1)
        request.delete()
        self.assertEqual(Action.objects.filter(model='hello.request',
                                               action='delete').count(),
                         1)
