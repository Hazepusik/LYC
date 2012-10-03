from django.conf.urls import patterns, include, url
from News.views import *
from Menu.views import *
from Page.views import *
from Comments.views import *
from Answer.views import *
from Storage.views import *
from Albums.views import *
from Fotogalery.views import *

from django.views.static import *
from django.conf import settings


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
    url(r'^menu/(?P<menupoint>\w+)/$',SubmenuOut),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^News/$', NewsOut ),
    url(r'^$', MenuOut ),
    url(r'^pages/(?P<pageid>\w+)/$', PageOut ),
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
    url(r'^del_answer/(?P<comid>\w+)/$', DelAns ),
    url(r'^add_answer/(?P<comid>\w+)/$', AddAns ),
    url(r'^control/news/add/$', NewsToAdd ),
    url(r'^add_news/$', AddNews ),
    url(r'^control/news/edit/(?P<newwid>\w+)/$', EdNewsOut ),
    url(r'^edit_news/(?P<newwid>\w+)/$', EditNews ),
    url(r'^del_news/(?P<newwid>\w+)/$', DelNews ),
    url(r'^control/news/$', ContrNewsOut ),
    url(r'^control/menu/$', ContrMenuOut ),
    url(r'^control/file/add/$', FileToAdd ),
    url(r'^add_file/$', AddFile ),
    url(r'^control/galery/add/$', GalerToAdd ),
    url(r'^add_galery/$', AddGaler ),
    url(r'^Galery/$', GalerOut ),
    url(r'^edit_galery/(?P<imgid>\w+)/$', EditGaler ),
    url(r'^control/galery/edit/(?P<imgid>\w+)/$', GalerToEdit),
    url(r'^del_file/(?P<fid>\w+)/$', DelFile),
    url(r'^control/galery/$', ContrGalerOut ),
    url(r'^Video/$', VideoOut ),
    url(r'^control/video/$', ContrVideoOut ),
    url(r'^control/video/add/$', VideoToAdd ),
    url(r'^add_video/$', AddVideo ),
    url(r'^edit_video/(?P<vidid>\w+)/$', EditVideo ),
    url(r'^control/video/edit/(?P<vidid>\w+)/$', VideoToEdit),
    url(r'^control/file/assign/(?P<pgid>\w+)/$', PgFileToAdd ),
    url(r'^assign_file/(?P<pgid>\w+)/$', AddPgFile ),
    url(r'^edit_file/(?P<fid>\w+)/$', EditFile ),
    url(r'^control/file/edit/(?P<fid>\w+)/$', FileToEdit),
    url(r'^control/file/pictopage/(?P<pgid>\w+)/$', PicFileToAdd ),
    url(r'^addpic_file/(?P<pgid>\w+)/$', AddPicFile ),
    url(r'^control/fotogalery/album/add/$', AlbumToAdd),
    url(r'^add_album/$', AddAlbum ),
    url(r'^control/fotogalery/$', ContrFotogaleryOut ),
    url(r'^del_album/(?P<albid>\w+)/$', DelAlbum),
    url(r'^Fotogalery/$', FotogaleryOut ),
    url(r'^Albums/(?P<albid>\w+)/$', AlbumOut ),     
    url(r'^control/fotogalery/album/(?P<albid>\w+)/$', ContrAlbumOut ),
    url(r'^control/fotogalery/foto/add/(?P<albid>\w+)/$', FotoToAdd ),
    url(r'^add_foto/(?P<albid>\w+)/$', AddFoto ),
    url(r'^del_foto/(?P<fid>\w+)/$', DelFoto),
    url(r'^control/fotogalery/foto/edit/(?P<fid>\w+)/$', FotoToEdit ),
    url(r'^edit_foto/(?P<fid>\w+)/$', EditFoto ),
    url(r'^control/fotogalery/album/edit/(?P<albid>\w+)/$', AlbumToEdit),
    url(r'^edit_album/(?P<albid>\w+)/$', EditAlbum),
    url(r'^control/answer/edit/(?P<comid>\w+)/$', AnsToEdit ),
    url(r'^edit_answer/(?P<comid>\w+)/$', EditAns ),
    url(r'^Search/$', WordToSearch ),  
    url(r'^search_word/$', SearchWord ),
)
