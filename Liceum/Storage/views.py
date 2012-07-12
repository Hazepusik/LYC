# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
import mimetypes
import os

from Storage.models import StorageCell
from Page.models import Page


def get_type(fname):
    mimetypes.init()
    try:
        header = mimetypes.types_map["."+fname.split(".")[-1]]
    except:
        header = "unknown"
    return header.split("/")[0][:3]


def FileToAdd(request):
    if request.user.is_authenticated():
        pglist = Page.objects.order_by('position')
        return render_to_response('control/file/add.html', {'Pages':pglist}, context_instance = RequestContext(request))


def AddFile(request):
    if request.user.is_authenticated():
        if request.POST['visible'] == "True":
            vis = True
        else:
            vis = False
        file = request.FILES['upfile']
        f =StorageCell(name = request.POST['name'], visible = vis, subj = file, filetype = get_type(file.name), page = Page.objects.get(id = request.POST['list']))
        f.save()
        return redirect('/control/file/add')

def GalerToAdd(request):
    if request.user.is_authenticated():
        pglist = Page.objects.order_by('position')
        return render_to_response('control/galery/add.html', {'Pages':pglist}, context_instance = RequestContext(request))


def AddGaler(request):
    if request.user.is_authenticated():
        if request.POST['visible'] == "True":
            vis = True
        else:
            vis = False
        file = request.FILES['upfile']
        f = StorageCell(name = request.POST['name'], visible = vis, subj = file, filetype = 'galer', page = Page.objects.get(id = request.POST['list']))
        f.save()
        return redirect('/control/galery/')
    
def GalerOut(request):	
    gal = StorageCell.objects.filter(visible = True).filter(filetype = 'galer')
    temp = loader.get_template('Galery.html')
    cont = Context({'Files': gal})
    return HttpResponse(temp.render(cont))
   
def GalerToEdit(request, imgid):
    if request.user.is_authenticated():
        pglist = Page.objects.order_by('position')
        img = StorageCell.objects.get(id = imgid)
        pth = img.subj.path
        return render_to_response('control/galery/edit.html', {'Pages':pglist, 'img':img, 'pth': pth}, context_instance = RequestContext(request))


def EditGaler(request, imgid):
    if request.user.is_authenticated():
        if request.POST['visible'] == "True":
            vis = True
        else:
            vis = False
        file = request.FILES['upfile']
        f = StorageCell.objects.get(id=imgid)
        f.name = request.POST['name']
        f.visible = vis
        f.subj = file
        if f.subj.path != request.POST['pth'] and (f.subj.path != ''):
            os.remove(request.POST['pth'])    
        f.filetype = 'galer'
        f.page = Page.objects.get(id = request.POST['list'])
        f.save()
        return redirect('/control/galery/')

#haz
def DelFile(request, fid):
    if request.user.is_authenticated():
        f = StorageCell.objects.get(id=fid)
        os.remove(f.subj.path)
        where = 'file'
        if f.filetype == 'galer':
            where = 'galery'
        if f.filetype == 'video':
            where = 'video'
     
        f.delete() 
        return redirect('/control/'+where+'/')
    
#haz
def ContrGalerOut(request):    
    if request.user.is_authenticated():
        f = StorageCell.objects.filter(filetype = 'galer').order_by('id')
        cont = Context({'Files':f})
        return render_to_response('control/galery.html', cont, context_instance = RequestContext(request))
  
#haz  
def VideoOut(request):	
    vid = StorageCell.objects.filter(visible = True).filter(filetype = 'video')
    temp = loader.get_template('Video.html')
    cont = Context({'Files': vid})
    return HttpResponse(temp.render(cont))

#haz
def VideoToAdd(request):
    if request.user.is_authenticated():
        pglist = Page.objects.order_by('position')
        return render_to_response('control/video/add.html', {'Pages':pglist}, context_instance = RequestContext(request))

#haz
def AddVideo(request):
    if request.user.is_authenticated():
        if request.POST['visible'] == "True":
            vis = True
        else:
            vis = False
        file = request.FILES['upfile']
        f = StorageCell(name = request.POST['name'], visible = vis, subj = file, filetype = 'video', page = Page.objects.get(id = request.POST['list']))
        f.save()
        return redirect('/control/video/')
    
    
#haz
def ContrVideoOut(request):    
    if request.user.is_authenticated():
        f = StorageCell.objects.filter(filetype = 'video').order_by('id')
        cont = Context({'Files':f})
        return render_to_response('control/video.html', cont, context_instance = RequestContext(request))

#haz    
def VideoToEdit(request, vidid):
    if request.user.is_authenticated():
        pglist = Page.objects.order_by('position')
        vid = StorageCell.objects.get(id = vidid)
        pth = vid.subj.path
        return render_to_response('control/video/edit.html', {'Pages':pglist, 'vid':vid, 'pth': pth}, context_instance = RequestContext(request))


#haz
def EditVideo(request, vidid):
    if request.user.is_authenticated():
        if request.POST['visible'] == "True":
            vis = True
        else:
            vis = False
        file = request.FILES['upfile']
        f = StorageCell.objects.get(id=vidid)
        f.name = request.POST['name']
        f.visible = vis
        f.subj = file
        if (f.subj.path != request.POST['pth']) and (f.subj.path != '')  :
            os.remove(request.POST['pth'])    
        f.filetype = 'video'
        f.page = Page.objects.get(id = request.POST['list'])
        f.save()
        return redirect('/control/video/')
    
#haz   
def PgFileToAdd(request,pgid):
    if request.user.is_authenticated():
        return render_to_response('control/file/assign.html', {'pgid':pgid}, context_instance = RequestContext(request))
    
#haz
def AddPgFile(request, pgid):
    if request.user.is_authenticated():
        if request.POST['visible'] == "True":
            vis = True
        else:
            vis = False
        file = request.FILES['upfile']
        f =StorageCell(name = request.POST['name'], visible = vis, subj = file, filetype = get_type(file.name), page = Page.objects.get(id = pgid))
        f.save()
        return redirect('/control/page/edit/'+pgid+'/')
