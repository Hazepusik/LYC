# Create your views here.
# -*- coding: utf-8 -*-
import re
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.template import loader, Context
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
import mimetypes
import os

from Storage.models import StorageCell
from Page.models import Page
from Menu.models import Menu


def del_tags_from_str(str):
    ultimate_regexp = "(?i)<\/?\w+((\s+\w+(\s*=\s*(?:\".*?\"|'.*?'|[^'\">\s]+))?)+\s*|\s*)\/?>"
    return re.sub(ultimate_regexp, "", str)


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
        id = 'edit/'+str(f.page.id)+'/'
        os.remove(f.subj.path)
        where = 'page'
        if f.filetype == 'galer':
            where = 'galery'
            id =''
        if f.filetype == 'video':
            where = 'video'
            id = ''
        f.delete() 
        return redirect('/control/'+where+'/'+id)
    
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

#haz
def FileToEdit(request, fid):
    if request.user.is_authenticated():
        pglist = Page.objects.order_by('position')
        file = StorageCell.objects.get(id = fid)
        pth = file.subj.path
        return render_to_response('control/file/edit.html', {'Pages':pglist, 'file':file, 'pth': pth}, context_instance = RequestContext(request))

#haz
def EditFile(request, fid):
    if request.user.is_authenticated():
        if request.POST['visible'] == "True":
            vis = True
        else:
            vis = False
        file = request.FILES['upfile']
        f = StorageCell.objects.get(id=fid)
        f.name = request.POST['name']
        f.visible = vis
        f.subj = file
        if f.subj.path != request.POST['pth'] and (f.subj.path != ''):
            os.remove(request.POST['pth'])    
        f.filetype = get_type(file.name)
        f.page = Page.objects.get(id = request.POST['list'])
        f.save()
        return render('/control/page/edit/'+ request.POST['list']+'/')
    
#haz   
def PicFileToAdd(request,pgid):
    if request.user.is_authenticated():
        return render_to_response('control/file/pictopage.html', {'pgid':pgid }, context_instance = RequestContext(request))
    
#haz
def AddPicFile(request, pgid):
    if request.user.is_authenticated():
        file = request.FILES['upfile']
        if get_type(file.name) == 'ima':
            f = StorageCell(name = request.POST['name'], visible = False, subj = file, filetype = 'picpg', page = Page.objects.get(id = pgid))
            f.save()
            return redirect('/control/page/edit/'+pgid+'/' )
        else:
            err = 'File isn''t an image'
            temp = loader.get_template('error.html')
            cont = Context({'errtext': err})
            return HttpResponse(temp.render(cont))                   


def SearchWord(str):
    menus = Menu.objects.filter( Q(visible = True) | Q(text = 'left') ).exclude(text = 'video')
    pages = Page.objects.none()
    for menu in menus:
        pages = pages | Page.objects.filter(Q(visible = True)).filter(menupoint = menu) #.filter( Q(text__contains=str) | Q(name__contains=str) )
    for page in pages:
        ultimate_regexp = "(?i)<\/?\w+((\s+\w+(\s*=\s*(?:\".*?\"|'.*?'|[^'\">\s]+))?)+\s*|\s*)\/?>"
        p = re.compile(ultimate_regex)
        p.sub('', html)
        