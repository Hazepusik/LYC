from django.conf.urls import patterns, include, url
from News.views import *
from Menu.views import *
from Page.views import *
from Comments.views import *
from Answer.views import *


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
    url(r'^control/page/add/$', PgMenuToAdd ),
    url(r'^add_page/$', AddPage ),
    url(r'^control/page/edit/(?P<pageid>\w+)/$', EdPgOut ),
    url(r'^edit_page/(?P<pageid>\w+)/$', EditPage ),
    url(r'^control/menu/add/$', MenuToAdd ),
    url(r'^add_menu/$', AddMenu ),
    url(r'^control/menu/edit/(?P<menuid>\w+)/$', EdMenuOut ),
    url(r'^edit_menu/(?P<menuid>\w+)/$', EditMenu ),
    url(r'^del_menu/(?P<menuid>\w+)/$', DelMenu ),
    url(r'^addcomment/(?P<whom>\w+)/$', CommToAdd ),
    url(r'^add_comment/(?P<whom>\w+)/$', AddComm ),
    url(r'^control/comments/(?P<whom>\w+)/$', ContrCommOut ),
    url(r'^del_comment/(?P<comid>\w+)/$', DelComm ),
    url(r'^comments/(?P<whom>\w+)/$', CommOut ),
    url(r'^control/answer/add/(?P<comid>\w+)/$', AnsToAdd ),
    url(r'^add_answer/(?P<comid>\w+)/$', AddAns ),
    url(r'^control/news/add/$', NewsToAdd ),
    url(r'^add_news/$', AddNews ),
    url(r'^control/news/edit/(?P<newwid>\w+)/$', EdNewsOut ),
    url(r'^edit_news/(?P<newwid>\w+)/$', EditNews ),
    url(r'^del_news/(?P<newwid>\w+)/$', DelNews ),
    url(r'^control/news/$', ContrNewsOut ),
    url(r'^control/menu/$', ContrMenuOut ),
	url(r'^control/page/(?P<menuid>\w+)/$', ShowMenu),
)
