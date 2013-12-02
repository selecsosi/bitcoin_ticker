# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
import calendar

from ticker.models import Quote
import itertools

def quotes(request):
    ql_sell = Quote.objects.filter(quote_type__name="sell").order_by('-modified')[:500]
    ql_buy = Quote.objects.filter(quote_type__name="buy").order_by('-modified')[:500]

    x_sell_data = [calendar.timegm(x.modified.timetuple()) * 1000 for x in ql_sell]
    ydata1 = [float(x.price) for x in ql_sell]
    ydata2 = [float(x.price) for x in ql_buy]





    tooltip_date = "%d %b %Y %H:%M:%S %p"
    extra_serie = {"tooltip": {"y_start": "$ ", "y_end": ""},
                    "date_format": tooltip_date}

    chartdata = {
        'x': x_sell_data,
        'name1': 'sell', 'y1': ydata1, 'extra1': extra_serie,
        'name2': 'buy', 'y2': ydata2, 'extra2': extra_serie,
    }

    charttype = "lineChart"
    chartcontainer = 'linechart_container'  # container name
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
        'kill_everythin': x_sell_data,
    }

    return render_to_response('ticker/quotes.html', data)