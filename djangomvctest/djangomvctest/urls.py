from django.conf.urls import patterns, include, url

from django.contrib import admin
from djangomvctestapp import viewkategori


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangomvctest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^kategoriler1/$', viewkategori.get_kategori_list1),
    url(r'^kategoriler2/$', viewkategori.get_kategori_list2),
)
