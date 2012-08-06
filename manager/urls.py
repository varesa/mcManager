from django.conf.urls import patterns, url, include

from django.contrib import admin
admin.autodiscover()

urlpatterns = \
patterns('',
# Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

     # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
) + \
patterns('manager.views',
    url(r'^login/$',                            'login_'),
    url(r'^login/(?P<location>[.\w]+)/$',       'login_'),
    #url(r'^login/(?P<location>[.\w]+)/$',       'login_'),
    url(r'^login_action/$',                     'login_action'),
    url(r'^logout$',                            'logout_action'),
    
    url(r'^$', 'index'),
    url(r'^status/$',                           'status_index'),
    url(r'^status/index/$',                     'status_index'),
    
    url(r'^_start_server/(?P<serverid>\d+)/$',  'start_server'),
    url(r'^_stop_server/(?P<serverid>\d+)/$',   'stop_server'),
    
    
    url(r'^manage/$',                           'manage_index'),
    url(r'^manage/index/$',                     'manage_index'),
    url(r'^manage/index/(?P<serverid>\d+)/$',   'manage_index'),
    
    url(r'^admin_/$',                        	'admin_index'),
    url(r'^admin_/index/$',                  	'admin_index'),
        url(r'^admin/users/$',                 	  'admin_users'),
        url(r'^admin/permissions/$',              'admin_permissions'),
        url(r'^admin/settings/$',                 'admin_settings'),
    
    #url(r'^create_server$','create_server'),
)
