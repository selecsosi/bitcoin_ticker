# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Quote.from_currency'
        db.add_column(u'ticker_quote', 'from_currency',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='from_currency', to=orm['ticker.Currency']),
                      keep_default=False)

        # Adding field 'Quote.to_currency'
        db.add_column(u'ticker_quote', 'to_currency',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='to_currency', to=orm['ticker.Currency']),
                      keep_default=False)

        # Removing M2M table for field to_currency on 'Quote'
        db.delete_table(db.shorten_name(u'ticker_quote_to_currency'))

        # Removing M2M table for field from_currency on 'Quote'
        db.delete_table(db.shorten_name(u'ticker_quote_from_currency'))


    def backwards(self, orm):
        # Deleting field 'Quote.from_currency'
        db.delete_column(u'ticker_quote', 'from_currency_id')

        # Deleting field 'Quote.to_currency'
        db.delete_column(u'ticker_quote', 'to_currency_id')

        # Adding M2M table for field to_currency on 'Quote'
        m2m_table_name = db.shorten_name(u'ticker_quote_to_currency')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('quote', models.ForeignKey(orm[u'ticker.quote'], null=False)),
            ('currency', models.ForeignKey(orm[u'ticker.currency'], null=False))
        ))
        db.create_unique(m2m_table_name, ['quote_id', 'currency_id'])

        # Adding M2M table for field from_currency on 'Quote'
        m2m_table_name = db.shorten_name(u'ticker_quote_from_currency')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('quote', models.ForeignKey(orm[u'ticker.quote'], null=False)),
            ('currency', models.ForeignKey(orm[u'ticker.currency'], null=False))
        ))
        db.create_unique(m2m_table_name, ['quote_id', 'currency_id'])


    models = {
        u'ticker.currency': {
            'Meta': {'object_name': 'Currency'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'ticker.exchange': {
            'Meta': {'object_name': 'Exchange'},
            'base_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'ticker.exchangeendpoint': {
            'Meta': {'object_name': 'ExchangeEndpoint'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ticker.Currency']"}),
            'exchange': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ticker.Exchange']"}),
            'fetch_interval': ('django.db.models.fields.IntegerField', [], {'default': '15', 'max_length': '8'}),
            'fetch_interval_scale': ('django.db.models.fields.IntegerField', [], {'default': '60000', 'max_length': '16'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'path_url': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'quote_types': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'+'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['ticker.QuoteType']"})
        },
        u'ticker.quote': {
            'Meta': {'object_name': 'Quote'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'exchange_endpoint': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ticker.ExchangeEndpoint']"}),
            'exchange_timestamp': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'from_currency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from_currency'", 'to': u"orm['ticker.Currency']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': 'None', 'null': 'True', 'max_digits': '16', 'decimal_places': '8'}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'default': 'None', 'null': 'True', 'max_digits': '16', 'decimal_places': '8'}),
            'quote_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ticker.QuoteType']"}),
            'to_currency': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to_currency'", 'to': u"orm['ticker.Currency']"})
        },
        u'ticker.quotetype': {
            'Meta': {'object_name': 'QuoteType'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['ticker']