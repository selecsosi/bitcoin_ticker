__author__ = 'sam'

from django.conf.urls import patterns, include, url
from .api.resources import QuoteResource, QuoteTypeResource
from tastypie.api import Api

v1_api = Api(api_name='v1')
v1_api.register(QuoteTypeResource())
v1_api.register(QuoteResource())

urlpatterns = patterns('ticker.views',
    (r'^quotes/', 'quotes'),
    (r'^api/', include(v1_api.urls)),
)

