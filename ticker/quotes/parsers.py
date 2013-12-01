__author__ = 'sam'


class BaseExchangeParser(object):

    endpoint = None

    def get_quote(self):
        raise NotImplementedError("Subclass must implement {}"
            .format(self.get_quote.__name__))


class MtGoxExchangeParser(BaseExchangeParser):





    pass



