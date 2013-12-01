from .models import MtGoxBTCUSDMoneyFastTickerModel

__author__ = 'sam'


class MtGoxBTCUSDMoneyFastTickerDecoder(object):
    @classmethod
    def decode_object(cls, obj):
        if issubclass(obj, dict):
            if obj["result"] == "success":
                buy = {"price": 0}
                sell = {"price": 0}
                last = {"price": 0}
                last_local = {"price": 0}
                last_orig = {"price": 0}
                last_all = {"price": 0}
                now = 0
                if "now" in obj:
                    now = obj["now"]
                if "data" in obj:
                    data = obj["data"]
                    if "buy" in data:
                        buy["price"] = data["buy"]["price"]
                    if "sell" in data:
                        sell["price"] = data["sell"]["price"]
                    if "last" in data:
                        last["price"] = data["last"]["price"]
                    if "last_local" in data:
                        last_local["price"] = data["last_local"]["price"]
                    if "last_orig" in data:
                        last_orig["price"] = data["last_orig"]["price"]
                    if "last_all" in data:
                        last_all["price"] = data["last_all"]["price"]

                return MtGoxBTCUSDMoneyFastTickerModel(buy, sell, last, last_local, last_orig, last_all, now)
            else:
                return None
        else:
            return None