# Create your views here.
from django.http import HttpResponseRedirect
from django.template import loader, Context
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
import os

from Storage.models import StorageCell
from Albums.models import Album
from Fotogalery.models import Foto


#haz
def AlbumToAdd(request):
    if request.user.is_authenticated():
        return render_to_response('control/fotogalery/album/add.html', {}, context_instance = RequestContext(request))
    
#haz
def AddAlbum(request):
    if request.user.is_authenticated():
        if request.POST['visible'] == "True":
            vis = True
        else:
            vis = False
        f = Album(name = request.POST['name'], visible = vis, text = request.POST['text'])
        f.save()
        return redirect('/control/fotogalery/album/'+str(f.id)+'/')

#haz
def ContrFotogaleryOut(request):    
    if request.user.is_authenticated():
        alb = Album.objects.order_by('id')
        cont = Context({'Albums':alb})
        return render_to_response('control/fotogalery.html', cont, context_instance = RequestContext(request))
    
    
#haz
def DelAlbum(request, albid):
    if request.user.is_authenticated():
        alb = Album.objects.get(id=albid)
        fs = Foto.objects.filter(album =alb)
        for f in fs:
            os.remove(f.subj.path)
            f.delete() 
        alb.delete()
        return redirect('/control/fotogalery/')

#haz  
def FotogaleryOut(request):	
    alb = Album.objects.filter(visible = True).order_by('date')
    temp = loader.get_template('Fotogalery.html')
    cont = Context({'Albums': alb})
    return HttpResponse(temp.render(cont))

#haz  
def AlbumOut(request, albid):
    alb = Album.objects.get(id=albid)
    foto = Foto.objects.filter(visible = True).filter(album = alb).order_by('id')
    temp = loader.get_template('Albums.html')
    cont = Context({'Fotos': foto})
    return HttpResponse(temp.render(cont))

#haz
def ContrAlbumOut(request, albid):    
    if request.user.is_authenticated():
        alb = Album.objects.get(id=albid)
        foto = Foto.objects.filter(album = alb).order_by('id')
        cont = Context({'Fotos': foto, 'album':alb})
        return render_to_response('control/fotogalery/album.html', cont, context_instance = RequestContext(request))

#haz
def FotoToAdd(request, albid):
    if request.user.is_authenticated():
        return render_to_response('control/fotogalery/foto/add.html', {'albid':albid}, context_instance = RequestContext(request))

#haz
def AddFoto(request, albid):
    if request.user.is_authenticated():
        if request.POST['visible'] == "True":
            vis = True
        else:
            vis = False
        file = request.FILES['upfile']
        #FIXIT
        f = Foto(name = request.POST['name'], visible = vis, subj = file, text = request.POST['text'], album = Album.objects.get(id=albid))
        f.save()
        return redirect('/control/fotogalery/album/'+str(albid)+'/')
    
#haz
def DelFoto(request, fid):
    if request.user.is_authenticated():
        fs = Foto.objects.get(id = fid)
        albid = fs.album.id
        os.remove(fs.subj.path)
        fs.delete() 
        return redirect('/control/fotogalery/album/'+str(albid)+'/')
    
#haz
def FotoToEdit(request, fid):
    if request.user.is_authenticated():
        f = Foto.objects.get(id = fid)
        return render_to_response('control/fotogalery/foto/edit.html', {'fid':fid, 'foto' : f}, context_instance = RequestContext(request))

#haz
def EditFoto(request, fid):
    if request.user.is_authenticated():
        if request.POST['visible'] == "True":
            vis = True
        else:
            vis = False
        file = request.FILES['upfile']
        #FIXIT
        f = Foto.objects.get(id = fid)
        f.name = request.POST['name']
        f.visible = vis
        f.subj = file
        f.text = request.POST['text']
        albid = f.album.id
        f.save()
        return redirect('/control/fotogalery/album/'+str(albid)+'/')

#haz
def AlbumToEdit(request, albid):
    if request.user.is_authenticated():
        alb = Album.objects.get(id = albid)
        return render_to_response('control/fotogalery/album/edit.html', {'alb' : alb}, context_instance = RequestContext(request))
    
#haz
def EditAlbum(request, albid):
    if request.user.is_authenticated():
        if request.POST['visible'] == "True":
            vis = True
        else:
            vis = False
        f = Album.objects.get(id = albid)
        f.name = request.POST['name']
        f.visible = vis
        f.text = request.POST['text']
        f.save()
        return redirect('/control/fotogalery/album/'+str(f.id)+'/')
