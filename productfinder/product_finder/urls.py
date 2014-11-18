from django.conf.urls import patterns, include, url
from product_finder import views

urlpatterns = patterns('',
		url(r'^$',views.index,name='index'),
		url(r'^category/(?P<category_type_url>\w+)/$',views.category,name='category'),
		url(r'^category/(?P<category_type_url>\w+)/(?P<request_productName_url>\w+)/$',views.request,name='request'),
    # Examples:
    # url(r'^$', 'productfinder.views.home', name='home'),
    # url(r'^productfinder/', include('productfinder.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
