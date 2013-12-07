import json
from datetime import datetime
import pytz
from django.conf import settings
from ..models import Quote
from django.utils import timezone

class BaseExchangeParser(object):

    exchange_endpoint = None

    def __init__(self, exchange_endpoint):
        self.exchange_endpoint = exchange_endpoint
        self.quote_types = { x.name: x  for x in self.exchange_endpoint.supported_quote_types.all()}

    def parse_response(self, response):
        """
        """
        raise NotImplementedError("Subclass must implement {}"
            .format(self.parse_response.__name__))

class MtGoxExchangeMoneyFastTickerParser(BaseExchangeParser):

    def parse_response(self, response_json):
        model = json.loads(response_json)
        quote_list = []
        if isinstance(model, dict):
            if model["result"] == "success":
                local_tz = pytz.timezone(settings.TIME_ZONE)
                timestamp_dt = timezone.now()
                if "now" in model:
                    timestamp = model["now"]
                    timestamp_dt = datetime.fromtimestamp(timestamp, tz=timezone.get_current_timezone())
                if "data" in model:
                    data = model["data"]
                    for key in data.keys():
                        if key in self.quote_types:
                            quote_type = self.quote_types[key]
                            quote = Quote()
                            quote.quote_type = quote_type
                            quote.exchange_endpoint = self.exchange_endpoint
                            quote.from_currency = self.exchange_endpoint.from_currency
                            quote.to_currency = self.exchange_endpoint.to_currency
                            quote.price = data[key].get("value", 0)
                            quote.exchange_timestamp = timestamp_dt
                            quote_list.append(quote)

        return quote_list


class MtGoxExchangeMoneyTickerParser(BaseExchangeParser):

    quantity_quote_keys = ('vol', )

    def parse_response(self, response_json):
        model = json.loads(response_json)
        quote_list = []
        if isinstance(model, dict):
            if model.get("result", None) == "success":
                local_tz = pytz.timezone(settings.TIME_ZONE)
                timestamp_dt = timezone.now()
                if "now" in model:
                    timestamp = model["now"]
                    timestamp_dt = datetime.fromtimestamp(timestamp, tz=timezone.get_current_timezone())
                if "data" in model:
                    data = model["data"]
                    for key in data.keys():
                        if key in self.quote_types:
                            quote_type = self.quote_types[key]
                            quote = Quote()
                            quote.quote_type = quote_type
                            quote.exchange_endpoint = self.exchange_endpoint
                            quote.from_currency = self.exchange_endpoint.from_currency
                            quote.to_currency = self.exchange_endpoint.to_currency
                            if key in self.quantity_quote_keys:
                                quote.quantity = data[key].get("value", 0)
                            else:
                                quote.price = data[key].get("value", 0)
                            quote.exchange_timestamp = timestamp_dt
                            quote_list.append(quote)

        return quote_list

class BitstampExchangeTickerParser(BaseExchangeParser):

    key_map = {
        "high": "high",
        "last": "last",
        "timestamp": "timestamp",
        "bid": "buy",
        "low": "low",
        "ask": "sell",
    }


    quantity_quote_keys = ('vol', )

    def parse_response(self, response_json):
        model = json.loads(response_json)
        quote_list = []
        if isinstance(model, dict):
            # local_tz = pytz.timezone(settings.TIME_ZONE)
            timestamp_dt = timezone.now()
            if "timestamp" in model:
                timestamp = model.pop("timestamp")
                timestamp_dt = datetime.fromtimestamp(timestamp, tz=timezone.get_current_timezone())

            for key in model.keys():
                if self.key_map[key] in self.quote_types:
                    quote_type = self.quote_types[self.key_map[key]]
                    quote = Quote()
                    quote.quote_type = quote_type
                    quote.exchange_endpoint = self.exchange_endpoint
                    quote.from_currency = self.exchange_endpoint.from_currency
                    quote.to_currency = self.exchange_endpoint.to_currency
                    if key in self.quantity_quote_keys:
                        quote.quantity = model[key]
                    else:
                        quote.price = model[key]
                    quote.exchange_timestamp = timestamp_dt
                    quote_list.append(quote)

        return quote_list