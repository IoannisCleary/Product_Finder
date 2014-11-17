from django.conf.urls import patterns, include, url
from product_finder import views

urlpatterns = patterns('',
		url(r'^$',views.index,name='index'),
		url(r'^request_page',views.request_page,name='request_page'),
    # Examples:
    # url(r'^$', 'productfinder.views.home', name='home'),
    # url(r'^productfinder/', include('productfinder.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
