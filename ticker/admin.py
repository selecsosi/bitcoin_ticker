from django.contrib import admin

# Register your models here.
from ticker.models import Exchange, Currency, ExchangeEndpoint, QuoteType, Quote, ExchangeEndpointParser


class ExchangeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Exchange, ExchangeAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Currency, CurrencyAdmin)

class ExhangeEndpointAdmin(admin.ModelAdmin):
    pass

admin.site.register(ExchangeEndpoint, ExhangeEndpointAdmin)

class QuoteTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(QuoteType, QuoteTypeAdmin)

class QuoteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Quote, QuoteAdmin)

class ExchangeEndpointParserAdmin(admin.ModelAdmin):
    pass

admin.site.register(ExchangeEndpointParser, ExchangeEndpointParserAdmin)
