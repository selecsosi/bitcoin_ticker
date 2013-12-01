__author__ = 'sam'

class MtGoxBTCUSDMoneyFastTickerModel(object):

    def __init__(self, buy, sell, last, last_local, last_orig, last_all, now):
        self.buy = buy
        self.sell = sell
        self.last = last
        self.last_local = last_local
        self.last_orig = last_orig
        self.last_all = last_all
        self.now = now


class MtGoxBTCUSDMoneyTickerModel(object):

    def __init__(self, buy, sell, last, last_local, last_orig, last_all, vol, avg, low, high, vwap, now):
        self.buy = buy
        self.sell = sell
        self.last = last
        self.last_local = last_local
        self.last_orig = last_orig
        self.last_all = last_all
        self.vol = vol
        self.avg = avg
        self.low = low
        self.high = high
        self.vwap = vwap
        self.now = now


