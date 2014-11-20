from django.conf.urls import patterns, include, url
from product_finder import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
		url(r'^product_finder/',include('product_finder.urls')),
		url(r'^admin/',include(admin.site.urls)),
		url(r'^comments/', include('django.contrib.comments.urls')),
    # Examples:
    # url(r'^$', 'productfinder.views.home', name='home'),
    # url(r'^productfinder/', include('productfinder.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
