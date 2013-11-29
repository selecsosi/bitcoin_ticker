# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Exchange'
        db.create_table(u'api_exchange', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('base_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['Exchange'])

        # Adding model 'Currency'
        db.create_table(u'api_currency', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'api', ['Currency'])

        # Adding model 'ExchangeEndpoint'
        db.create_table(u'api_exchangeendpoint', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exchange', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Exchange'])),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Currency'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('path_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['ExchangeEndpoint'])

        # Adding model 'QuoteType'
        db.create_table(u'api_quotetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['QuoteType'])

        # Adding model 'Quote'
        db.create_table(u'api_quote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quote_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.QuoteType'])),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=8)),
            ('exchange_endpoint', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.ExchangeEndpoint'])),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['api.Currency'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'api', ['Quote'])


    def backwards(self, orm):
        # Deleting model 'Exchange'
        db.delete_table(u'api_exchange')

        # Deleting model 'Currency'
        db.delete_table(u'api_currency')

        # Deleting model 'ExchangeEndpoint'
        db.delete_table(u'api_exchangeendpoint')

        # Deleting model 'QuoteType'
        db.delete_table(u'api_quotetype')

        # Deleting model 'Quote'
        db.delete_table(u'api_quote')


    models = {
        u'api.currency': {
            'Meta': {'object_name': 'Currency'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'api.exchange': {
            'Meta': {'object_name': 'Exchange'},
            'base_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'api.exchangeendpoint': {
            'Meta': {'object_name': 'ExchangeEndpoint'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Currency']"}),
            'exchange': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Exchange']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'path_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'api.quote': {
            'Meta': {'object_name': 'Quote'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.Currency']"}),
            'exchange_endpoint': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.ExchangeEndpoint']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '8'}),
            'quote_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['api.QuoteType']"})
        },
        u'api.quotetype': {
            'Meta': {'object_name': 'QuoteType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['api']