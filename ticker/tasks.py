
from datetime import timedelta

from celery.task import PeriodicTask
from .models import Exchange, ExchangeEndpoint
from .api.client import MtGoxExchangeMoneyFastTickerClient, MtGoxExchangeMoneyTickerClient
from ticker.api.client import BitstampExchangeTickerClient, Btc_eExchangeBtcUsdQuoteClient


class MtGoxExchangeMoneyFastTickerTask(PeriodicTask):
    run_every = timedelta(minutes=1)

    def run(self, **kwargs):
        exchange = Exchange.objects.get(name="MtGox")
        ee = ExchangeEndpoint.objects.get(exchange=exchange, name="Money Fast Ticker")
        mgerc = MtGoxExchangeMoneyFastTickerClient(ee)
        quote_list = mgerc.request_exchange_quotes()
        for quote in quote_list:
            quote.save()


class MtGoxExchangeMoneyTickerTask(PeriodicTask):
    run_every = timedelta(minutes=5)

    def run(self, **kwargs):
        exchange = Exchange.objects.get(name="MtGox")
        ee = ExchangeEndpoint.objects.get(exchange=exchange, name="Money Ticker")
        mgerc = MtGoxExchangeMoneyTickerClient(ee)
        quote_list = mgerc.request_exchange_quotes()
        for quote in quote_list:
            quote.save()


class BitstampExchangeTickerTask(PeriodicTask):
    run_every = timedelta(minutes=1)

    def run(self, **kwargs):
        exchange = Exchange.objects.get(name="Bitstamp")
        ee = ExchangeEndpoint.objects.get(exchange=exchange, name="Ticker")
        bsetc = BitstampExchangeTickerClient(ee)
        quote_list = bsetc.request_exchange_quotes()
        for quote in quote_list:
            quote.save()


class Btc_eExchangeBtcUsdTickerTask(PeriodicTask):
    run_every = timedelta(minutes=1)

    def run(self, **kwargs):
        exchange = Exchange.objects.get(name="Btc-e")
        ee = ExchangeEndpoint.objects.get(exchange=exchange, name="BTC:USD Ticker")
        btceqc = Btc_eExchangeBtcUsdQuoteClient(ee)
        quote_list = btceqc.request_exchange_quotes()
        for quote in quote_list:
            quote.save()
