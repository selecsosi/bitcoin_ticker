# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Exchange'
        db.create_table(u'ticker_exchange', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('site_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('base_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'ticker', ['Exchange'])

        # Adding model 'Currency'
        db.create_table(u'ticker_currency', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('symbol', self.gf('django.db.models.fields.CharField')(default='$', max_length=2)),
        ))
        db.send_create_signal(u'ticker', ['Currency'])

        # Adding model 'QuoteType'
        db.create_table(u'ticker_quotetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('details', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'ticker', ['QuoteType'])

        # Adding model 'ExchangeEndpoint'
        db.create_table(u'ticker_exchangeendpoint', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exchange', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ticker.Exchange'])),
            ('from_currency', self.gf('django.db.models.fields.related.ForeignKey')(related_name='from_currency', to=orm['ticker.Currency'])),
            ('to_currency', self.gf('django.db.models.fields.related.ForeignKey')(related_name='to_currency', to=orm['ticker.Currency'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('path_url', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('fetch_interval', self.gf('django.db.models.fields.IntegerField')(default=15, max_length=8)),
            ('fetch_interval_scale', self.gf('django.db.models.fields.IntegerField')(default=60000, max_length=16)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'ticker', ['ExchangeEndpoint'])

        # Adding M2M table for field supported_quote_types on 'ExchangeEndpoint'
        m2m_table_name = db.shorten_name(u'ticker_exchangeendpoint_supported_quote_types')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('exchangeendpoint', models.ForeignKey(orm[u'ticker.exchangeendpoint'], null=False)),
            ('quotetype', models.ForeignKey(orm[u'ticker.quotetype'], null=False))
        ))
        db.create_unique(m2m_table_name, ['exchangeendpoint_id', 'quotetype_id'])

        # Adding model 'Quote'
        db.create_table(u'ticker_quote', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exchange_endpoint', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ticker.ExchangeEndpoint'])),
            ('from_currency', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+from_currency', to=orm['ticker.Currency'])),
            ('to_currency', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+to_currency', to=orm['ticker.Currency'])),
            ('quote_type', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['ticker.QuoteType'])),
            ('quantity', self.gf('django.db.models.fields.DecimalField')(default=None, null=True, max_digits=16, decimal_places=8)),
            ('price', self.gf('django.db.models.fields.DecimalField')(default=None, null=True, max_digits=16, decimal_places=8)),
            ('exchange_timestamp', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'ticker', ['Quote'])


    def backwards(self, orm):
        # Deleting model 'Exchange'
        db.delete_table(u'ticker_exchange')

        # Deleting model 'Currency'
        db.delete_table(u'ticker_currency')

        # Deleting model 'QuoteType'
        db.delete_table(u'ticker_quotetype')

        # Deleting model 'ExchangeEndpoint'
        db.delete_table(u'ticker_exchangeendpoint')

        # Removing M2M table for field supported_quote_types on 'ExchangeEndpoint'
        db.delete_table(db.shorten_name(u'ticker_exchangeendpoint_supported_quote_types'))

        # Deleting model 'Quote'
        db.delete_table(u'ticker_quote')


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['ticker']