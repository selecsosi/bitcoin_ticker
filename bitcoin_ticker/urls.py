from django.conf.urls import patterns, include, url

from django.contrib import admin

from ticker.urls import v1_api as api

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bitcoin_ticker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^ticker/', include('ticker.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

