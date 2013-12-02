__author__ = 'sam'

from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.paginator import Paginator
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie import fields
from tastypie.cache import SimpleCache

from ..models import Quote, QuoteType

from .serializers import PrettyJSONSerializer

class QuoteTypeResource(ModelResource):

    def alter_list_data_to_serialize(self, request, data):
        data['quote_types'] = data['objects']
        del data['objects']
        return data

    def alter_deserialized_list_data(self, request, data):
        data['objects'] = data['quote_types']
        del data['quote_types']
        return data

    class Meta:
        queryset = QuoteType.objects.all()
        resource_name = 'quote_types'
        filtering = {'name': ('exact') }
        allowed_methods = ['get']
        cache = SimpleCache(timeout=60)
        serializer = PrettyJSONSerializer()


class QuoteResource(ModelResource):

    quote_type = fields.ToOneField(QuoteTypeResource, 'quote_type')

    def alter_list_data_to_serialize(self, request, data):
        data['quotes'] = data['objects']
        del data['objects']
        return data

    def alter_deserialized_list_data(self, request, data):
        data['objects'] = data['quotes']
        del data['api']
        return data

    def dehydrate(self, bundle):
        bundle.data["quote_type"] = bundle.obj.quote_type.name
        return bundle

    class Meta:
        queryset = Quote.objects.all().order_by('-modified')
        resource_name = 'quotes'
        filtering = { 'quote_type': ALL_WITH_RELATIONS }
        paginator_class = Paginator
        serializer = PrettyJSONSerializer()
        allowed_methods = ['get']
        cache = SimpleCache(timeout=60)
        # authorization= Authorization()