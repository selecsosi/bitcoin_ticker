# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
import calendar

from ticker.models import Quote, Exchange

from django.views.decorators.cache import cache_page

@cache_page(60)
def quotes(request, exchange_name="mtgox"):
    try:
        e = Exchange.objects.get(name__iexact=exchange_name)
    except Exchange.DoesNotExist:
        e = Exchange.objects.get(name__iexact="MtGox")

    ql_sell = Quote.objects.filter(quote_type__name="sell", exchange_endpoint__exchange=e).order_by('-modified')[:2000]
    ql_buy = Quote.objects.filter(quote_type__name="buy", exchange_endpoint__exchange=e).order_by('-modified')[:2000]
    ql_last = Quote.objects.filter(quote_type__name="last", exchange_endpoint__exchange=e).order_by('-modified')[:2000]

    x_sell = [calendar.timegm(x.modified.timetuple()) * 1000 for x in ql_sell]
    x_buy = [calendar.timegm(x.modified.timetuple()) * 1000 for x in ql_buy]
    x_last = [calendar.timegm(x.modified.timetuple()) * 1000 for x in ql_last]
    y_sell = [float(x.price) for x in ql_sell]
    y_buy = [float(x.price) for x in ql_buy]
    y_last = [float(x.price) for x in ql_last]

    # tooltip_date = "%d %b %Y %H:%M:%S %p"
    # extra_serie = {"tooltip": {"y_start": ql_sell[0].to_currency.symbol, "y_end": ""},
    #                 "date_format": tooltip_date}

    chartdata = {
        'name1': 'sell', 'x1': x_sell, 'y1': y_sell,
        'name2': 'buy', 'x2': x_buy, 'y2': y_buy,
        'name3': 'buy', 'x3': x_last, 'y3': y_buy,

    }

    charttype = "lineWithFocusChart"
    chartcontainer = 'linewithfocuschart_container'  # container name
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': True,
            'x_axis_format': '%H:%M:%S',
            'tag_script_js': True,
            'jquery_on_ready': False,
        },
    }

    return render_to_response('ticker/quotes.html', data)
