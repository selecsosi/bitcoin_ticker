import json
from ticker.models import Quote

__author__ = 'sam'


class BaseExchangeParser(object):

    exchange_endpoint = None

    def __init__(self, exchange_endpoint):
        self.exchange_endpoint = exchange_endpoint
        self.quote_types = { x.name: x  for x in self.exchange_endpoint.quote_types.all()}

    def parse_response(self, response):
        """
        """
        raise NotImplementedError("Subclass must implement {}"
            .format(self.parse_response.__name__))

class MtGoxExchangeMoneyFastTickerParser(BaseExchangeParser):

    def parse_response(self, response_json):
        model = json.loads(response_json)
        quote_list = []
        if issubclass(model, dict):
            if model["result"] == "success":
                now = 0
                if "now" in model:
                    now = model["now"]
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
                            quote.exchange_timestamp = now
                            quote_list.append(quote)

        return quote_list



