from django.conf.urls import patterns, include, url
from News.views import *
from Menu.views import *
from Page.views import *
from Comments.views import *


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Liceum.views.home', name='home'),
    # url(r'^Liceum/', include('Liceum.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^News/$', NewsOut ),
    url(r'^Menus/$', MenuOut ),
    url(r'^Pages/(?P<pageid>\w+)/$', PageOut ),
    url(r'^addpage/$', PgMenuToAdd ),
    url(r'^add_page/$', AddPage ),
    url(r'^editpage/(?P<pageid>\w+)/$', EdPgOut ),
    url(r'^edit_page/(?P<pageid>\w+)/$', EditPage ),
    url(r'^addmenu/$', MenuToAdd ),
    url(r'^add_menu/$', AddMenu ),
    url(r'^editmenu/(?P<menuid>\w+)/$', EdMenuOut ),
    url(r'^edit_menu/(?P<menuid>\w+)/$', EditMenu ),
    url(r'^addcomment/(?P<whom>\w+)/$', CommToAdd ),
    url(r'^add_comment/(?P<whom>\w+)/$', AddComm ),
    url(r'^del_comment/(?P<whom>\w+)/$', DelComm ),
    
    
)
