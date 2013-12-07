from .parsers import MtGoxExchangeMoneyFastTickerParser, MtGoxExchangeMoneyTickerParser
from ticker.api.parsers import BitstampExchangeTickerParser

__author__ = 'sam'
import requests
import gzip
import io
import json

class BaseRequestClient(object):

    def get_exchange_parser(self, exhchange_endpoint):
        raise NotImplementedError("")


class QuoteRequestClient(BaseRequestClient):

    def __init__(self, exhange_endpoint):
        self.exchange_endpoint = exhange_endpoint
        self.parser = self.get_exchange_parser(exhange_endpoint)

    def request_exchange_quotes(self):
        base_url = self.exchange_endpoint.exchange.base_url
        path_url = self.exchange_endpoint.path_url

        response = requests.get(base_url + path_url)
        return self.parse_response(response.text)
        
    def get_endpoint(self):
        return self.exchange_endpoint


    def parse_response(self, response):
        return self.parser.parse_response(response)


class MtGoxExchangeMoneyFastTickerClient(QuoteRequestClient):

    def __init__(self, exhange_endpoint):
        super(MtGoxExchangeMoneyFastTickerClient, self).__init__(exhange_endpoint)

    def get_exchange_parser(self, exhchange_endpoint):
        return MtGoxExchangeMoneyFastTickerParser(exhchange_endpoint)


class MtGoxExchangeMoneyTickerClient(QuoteRequestClient):

    def __init__(self, exhange_endpoint):
        super(MtGoxExchangeMoneyTickerClient, self).__init__(exhange_endpoint)

    def get_exchange_parser(self, exhchange_endpoint):
        return MtGoxExchangeMoneyTickerParser(exhchange_endpoint)

class BitstampExchangeTickerClient(QuoteRequestClient):

    def get_exchange_parser(self, exhchange_endpoint):
        return BitstampExchangeTickerParser(exhchange_endpoint)