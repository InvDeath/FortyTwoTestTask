# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Contacts.other_contacts'
        db.alter_column('hello_contacts', 'other_contacts', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):

        # Changing field 'Contacts.other_contacts'
        db.alter_column('hello_contacts', 'other_contacts', self.gf('django.db.models.fields.TextField')(default=''))

    models = {
        'hello.contacts': {
            'Meta': {'object_name': 'Contacts'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['hello']