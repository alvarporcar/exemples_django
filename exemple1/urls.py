from django.conf.urls.defaults import patterns, include, url
from exemple1.views import current_datetime
from exemple1.books.views import search

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^time/$',current_datetime),
    (r'^search/$', search),
    
    # Examples:
    # url(r'^$', 'exemple1.views.home', name='home'),
    
    # url(r'^exemple1/', include('exemple1.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
