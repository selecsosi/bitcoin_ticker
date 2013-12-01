__author__ = 'sam'


class BaseExchangeParser(object):

    exchange_endpoint = None

    def __init__(self, exchange_endpoint):
        self.exchange_endpoint = exchange_endpoint
        self.quote_types = { x.name: x  for x in self.exchange_endpoint.quote_types.all()}

    def parse_quote(self):
        raise NotImplementedError("Subclass must implement {}"
            .format(self.parse_quote.__name__))


class MtGoxExchangeParser(BaseExchangeParser):
    pass

