__author__ = 'sam'

from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.paginator import Paginator
from tastypie import fields

from .models import Quote, QuoteType

class QuoteTypeResource(ModelResource):
    quotes = fields.ToManyField('ticker.api.QuoteResource', 'quotes')

    def dehydrate(self, bundle):
        bundle.data = {"name" : bundle.data["name"]}
        return bundle

    class Meta:
        queryset = QuoteType.objects.all()
        resource_name = 'quote_type'



class QuoteResource(ModelResource):

    # quote_type = fields.ToOneField(QuoteTypeResource, 'quote_type')

    def dehydrate(self, bundle):
        bundle.data["quote_type"] = bundle.obj.quote_type.name
        return bundle

    class Meta:
        queryset = Quote.objects.all().order_by('-modified')
        resource_name = 'quote'
        paginator_class = Paginator
        allowed_methods = ['get']
        # authorization= Authorization()