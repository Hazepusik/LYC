# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from datetime import datetime

from Comments.models import Comment

def CommToAdd(request):	
    return render_to_response('addcomment.html', {}, context_instance = RequestContext(request))

def AddComm(request, whom):
    if request.POST['visible'] == "True":
        vis = True
    else:
        vis = False
    comm = Menu(text = request.POST['txt'], name = request.POST['name'], visible = vis, author = request.POST['author'], mailback = request.POST['mail'], thread = whom)
    comm.save()
    #FIXIT
    return redirect('/Menus/')

def DelComm(request, comid):
    Comment.objects.filter(id=com).delete()
    #FIXIT
    return redirect('/Menus/')