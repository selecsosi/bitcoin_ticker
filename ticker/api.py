__author__ = 'sam'

from tastypie.resources import ModelResource

from .models import Quote

class EntryResource(ModelResource):
    class Meta:
        queryset = Quote.objects.all()