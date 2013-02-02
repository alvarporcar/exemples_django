from django.conf.urls.defaults import patterns, include, url
from exemple1.views import current_datetime
from exemple1.books.views import search, contact


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^time/$',current_datetime),
    (r'^search/$', search),
    (r'^contact/$', contact),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
