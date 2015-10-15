from django.test import TestCase
from django.core.management import call_command
from StringIO import StringIO


class ManagementTestCase(TestCase):
    def test_all_modes(self):
        '''
        Test all models command
        '''
        buf = StringIO()
        call_command('all_models', stdout=buf, stderr=buf)
        self.assertIn('apps.hello.models.Request', buf.getvalue())
        self.assertIn('error: apps.hello.models.Request', buf.getvalue())
