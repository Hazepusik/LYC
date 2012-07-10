# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
import mimetypes


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
        #        f =StorageCell(name = request.POST['name'], visible = vis, subj = file['content'], filetype = get_type(file['filename']), page = Page.objects.get(id = request.POST['list']))

        f =StorageCell(name = request.POST['name'], visible = vis, subj = file, filetype = get_type(file.name), page = Page.objects.get(id = request.POST['list']))

        f.save()
        return redirect('/control/file/')
   