from django.db import models

class Exchange(models.Model):
    name = models.CharField(max_length=256, verbose_name="Exchange Name", null=False, blank=False)
    site_url = models.URLField(verbose_name="Exchange Site", null=False, blank=False)
    base_url = models.URLField(verbose_name="Exchange Base Url", null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    symbol = models.CharField(max_length=2, null=False, blank=False, default="$")

    def __unicode__(self):
        return self.name + " : " + self.symbol

    def __str__(self):
        return self.name + " : " + self.symbol


class QuoteType(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False, unique=True)
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
    from_currency = models.ForeignKey(Currency, related_name="from_currency")
    to_currency = models.ForeignKey(Currency, related_name="to_currency")
    supported_quote_types = models.ManyToManyField(QuoteType, blank=True, null=True, related_name="+")
    name = models.CharField(max_length=256, verbose_name="Endpoint Name", null=False, blank=False)
    path_url = models.CharField(max_length=256, null=False, blank=False, verbose_name="Exchange Endpoint Path")
    fetch_interval = models.IntegerField(max_length=8, verbose_name="Interval Value", blank=False, null=False, default=15)
    fetch_interval_scale = models.IntegerField(max_length=16, verbose_name="Interval Scale", choices=interval_scale_choices, blank=False, null=False, default=(60 * 1000))
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "{} {} {}".format(self.exchange.name, self.from_currency.name + ":" + self.to_currency.name, self.name)

    def __str__(self):
        return "{} {} {}".format(self.exchange.name, self.from_currency.name + ":" + self.to_currency.name, self.name)


class Quote(models.Model):
    exchange_endpoint = models.ForeignKey(ExchangeEndpoint)
    from_currency = models.ForeignKey(Currency, related_name="+from_currency")
    to_currency = models.ForeignKey(Currency, related_name="+to_currency")
    quote_type = models.ForeignKey(QuoteType)
    quantity = models.DecimalField(max_digits=16, decimal_places=8, blank=False, null=True, default=None)
    price = models.DecimalField(max_digits=16, decimal_places=8, blank=False, null=True, default=None)
    exchange_timestamp = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "{} {} {} {}".format(self.from_currency.name + ":" + self.to_currency.name, self.quote_type, "price :", self.price)

    def __str__(self):
        return "{} {} {} {}".format(self.from_currency.name + ":" + self.to_currency.name, self.quote_type, "price :", self.price)



