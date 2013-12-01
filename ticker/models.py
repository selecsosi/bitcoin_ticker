from django.db import models

# Create your models here.

class Exchange(models.Model):
    base_url = models.URLField(null=False, blank=False, verbose_name="Exchange Base Url")
    name = models.CharField(max_length=256, verbose_name="Exchange Name", null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class QuoteType(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    details = models.TextField(blank=True, null=False, default="")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class ExchangeEndpoint(models.Model):
    interval_scale_choices = (
        (1, 'milli'),
        (1000, 'second'),
        (60 * 1000, 'minute'),
        (3600 * 1000, 'hour'),
        (24 * 3600 * 1000, 'day'),
        (7 * 24 * 3600 * 1000, 'week'),
        (30 * 24 * 3600 * 1000, '30-day-month')
    )

    exchange = models.ForeignKey(Exchange)
    currency = models.ForeignKey(Currency)
    quote_types = models.ManyToManyField(QuoteType, blank=True, null=True, related_name="+")
    name = models.CharField(max_length=256, verbose_name="Endpoint Name", null=False, blank=False)
    path_url = models.CharField(max_length=256, null=False, blank=False, verbose_name="Exchange Endpoint Path")
    fetch_interval = models.IntegerField(max_length=8, verbose_name="Interval Value", blank=False, null=False, default=15)
    fetch_interval_scale = models.IntegerField(max_length=16, verbose_name="Interval Scale", choices=interval_scale_choices, blank=False, null=False, default=(60 * 1000))
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "{} {} {}".format(self.exchange.name, self.currency.name, self.name)

    def __str__(self):
        return "{} {} {}".format(self.exchange.name, self.currency.name, self.name)


class Quote(models.Model):
    quote_type = models.ForeignKey(QuoteType)
    price = models.DecimalField(max_digits=16, decimal_places=8, blank=False, null=False)
    exchange_endpoint = models.ForeignKey(ExchangeEndpoint)
    currency = models.ForeignKey(Currency)
    exchange_timestamp = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)