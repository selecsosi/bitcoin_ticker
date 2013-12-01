__author__ = 'sam'

from django.conf.urls import patterns, include, url
from .api import EntryResource

entry_resource = EntryResource()

urlpatterns = patterns('',
    (r'^api/', include(entry_resource.urls)),
)

