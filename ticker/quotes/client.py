__author__ = 'sam'
import requests
import gzip
import io
import json

class BaseRequestClient(object):
    pass


class QuoteRequestClient(object):


    def __init__(self, exchange, exhange_endpoint, quote_type):
        self.parser = self.get_exchange_parser(exhange_endpoint)

    def get_endpoint(self):
        pass

    def get_exchange_parser(self, exhchange_endpoint):
        pass



class MtGoxQuoteRequestClient(QuoteRequestClient):

    def sign_request(self, request):
        headers = {
            'User-Agent': "Trade-Bot",
            'Accept-Encoding': 'GZIP',
        }

    def get_quote(self):
        #make the request

        #parse the request
        response = requests.get("")
        x = {}
        enc = response.headers.get('Content-Encoding')
        if isinstance(enc, str) and enc.lower() == 'gzip':
            buff = io.BytesIO(response.content)
            response = gzip.GzipFile(fileobj=buff)

        output = json.load(response)


    def parse_response(self, response_json):
        new_quote_list = self.parser.parse(response_json)



    def get_endpoint(self):
        pass