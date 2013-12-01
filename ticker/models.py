from django.db import models

# Create your models here.

class Exchange(models.Model):
    base_url = models.URLField(null=False, blank=False, verbose_name="Exchange Base Url")
    name = models.CharField(max_length=256, verbose_name="Exchange Name", null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Currency(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)

class ExchangeEndpoint(models.Model):
    exchange = models.ForeignKey(Exchange)
    currency = models.ForeignKey(Currency)
    name = models.CharField(max_length=256, verbose_name="Endpoint Name", null=False, blank=False)
    path_url = models.URLField(null=False, blank=False, verbose_name="Exchange Path Url")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class QuoteType(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Quote(models.Model):
    quote_type = models.ForeignKey(QuoteType)
    price = models.DecimalField(max_digits=16, decimal_places=8, blank=False, null=False)
    exchange_endpoint = models.ForeignKey(ExchangeEndpoint)
    currency = models.ForeignKey(Currency)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)