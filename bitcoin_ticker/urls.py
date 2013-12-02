from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bitcoin_ticker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^ticker/', include('ticker.urls')),
    url(r'^admin/', include(admin.site.urls)),
)


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()