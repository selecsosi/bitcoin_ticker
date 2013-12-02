# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
import calendar

from ticker.models import Quote
import itertools

def quotes(request):
    ql_sell = Quote.objects.filter(quote_type__name="sell").order_by('-modified')[:500]
    ql_buy = Quote.objects.filter(quote_type__name="buy").order_by('-modified')[:500]

    x_sell_data = [calendar.timegm(x.modified.timetuple()) for x in ql_sell]
    ydata1 = [float(x.price) for x in ql_sell]
    ydata2 = [float(x.price) for x in ql_buy]
    # ydata2 = [str(x.price) for x in ql_buy]



    chartdata = {
        'x': x_sell_data,
        'name1': 'sell', 'y1': ydata1,
        'name2': 'buy', 'y2': ydata2,
    }
    charttype = "lineWithFocusChart"
    chartcontainer = 'linewithfocuschart_container'  # container name
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': True,
            'x_axis_format': '%d-%mT%H:%M:%S',
            'tag_script_js': True,
            'jquery_on_ready': False,
        },
    }

    return render_to_response('ticker/quotes.html', data)