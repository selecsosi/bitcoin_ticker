# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ExchangeEndpointParser'
        db.create_table(u'ticker_exchangeendpointparser', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exchange_endpoint', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ticker.ExchangeEndpoint'])),
            ('parser_module', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('parser_class', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal(u'ticker', ['ExchangeEndpointParser'])


    def backwards(self, orm):
        # Deleting model 'ExchangeEndpointParser'
        db.delete_table(u'ticker_exchangeendpointparser')


    models = {
        u'ticker.currency': {
            'Meta': {'object_name': 'Currency'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'symbol': ('django.db.models.fields.CharField', [], {'default': "'$'", 'max_length': '2'})
        },
        u'ticker.exchange': {
            'Meta': {'object_name': 'Exchange'},
            'base_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'site_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'ticker.exchangeendpoint': {
            'Meta': {'object_name': 'ExchangeEndpoint'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'exchange': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ticker.Exchange']"}),
            'fetch_interval': ('django.db.models.fields.IntegerField', [], {'default': '15', 'max_length': '8'}),
            'fetch_interval_scale': ('django.db.models.fields.IntegerField', [], {'default': '60000', 'max_length': '16'}),
            'from_currency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from_currency'", 'to': u"orm['ticker.Currency']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'path_url': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'supported_quote_types': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['ticker.QuoteType']"}),
            'to_currency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to_currency'", 'to': u"orm['ticker.Currency']"})
        },
        u'ticker.exchangeendpointparser': {
            'Meta': {'object_name': 'ExchangeEndpointParser'},
            'exchange_endpoint': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ticker.ExchangeEndpoint']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parser_class': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'parser_module': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'ticker.quote': {
            'Meta': {'object_name': 'Quote'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'exchange_endpoint': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ticker.ExchangeEndpoint']"}),
            'exchange_timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'from_currency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+from_currency'", 'to': u"orm['ticker.Currency']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': 'None', 'null': 'True', 'max_digits': '16', 'decimal_places': '8'}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'default': 'None', 'null': 'True', 'max_digits': '16', 'decimal_places': '8'}),
            'quote_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['ticker.QuoteType']"}),
            'to_currency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+to_currency'", 'to': u"orm['ticker.Currency']"})
        },
        u'ticker.quotetype': {
            'Meta': {'object_name': 'QuoteType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256'})
        }
    }

    complete_apps = ['ticker']