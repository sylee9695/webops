from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','login.views.index'),
    url(r'^index/$','login.views.index'),
    url(r'^login/$','login.views.login'),
    url(r'^logout/$','login.views.logout'),
    url(r'^accounts/login','login.views.index'),
    url(r'^dev_manage/$','devmanage.views.dev_view'),
    url(r'^ip_manage/$','devmanage.views.ip_view'),
    url(r'^add_ip/$','devmanage.views.add_ip'),
    url(r'^add_dev/$','devmanage.views.add_dev'),
    url(r'^search_ip/$','devmanage.views.search_ip'),
    url(r'^search_dev/$','devmanage.views.search_dev'),
    url(r'^mod_ip/$','devmanage.views.mod_ip'),
    url(r'^mod_dev/$','devmanage.views.mod_dev'),

)

