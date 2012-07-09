# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

from News.models import News

import datetime

def NewsOut(request):	
	newslist= News.objects.filter(visible = True)
	temp = loader.get_template('news.html')
	cont = Context({'NewsText':newslist})
	return HttpResponse(temp.render(cont))

def NewsToAdd(request):
    if request.user.is_authenticated():
        return render_to_response('control/news/add.html', {}, context_instance = RequestContext(request))


def AddNews(request):
    if request.user.is_authenticated():
        if request.POST['visible'] == "True":
            vis = True
        else:
            vis = False
        neww = News(name = request.POST['name'], visible = vis, text = request.POST['txt'], dateadd = request.POST['date'])
        neww.save()
        return redirect('/control/news/')
    
    
def EdNewsOut(request, newwid):	
    if request.user.is_authenticated():
        neww = News.objects.get(id = newwid)
        return render_to_response('control/news/edit.html', {'News':neww}, context_instance = RequestContext(request))


def EditNews(request, newwid):
    if request.user.is_authenticated():
        neww = News.objects.get(id = newwid)
        neww.text = request.POST['txt']
        if request.POST['vis'] == "True":
            neww.visible = True
        else:
            neww.visible = False
        neww.name = request.POST['name']
        
        #STATIC
        
        neww.dateadd = '1234-01-23'     #request.POST['date']
        neww.save()
        return redirect('/control/news/')
        #return render_to_response('control/news.html', {'News':neww}, context_instance = RequestContext(request))
    
def ContrNewsOut(request):    
    if request.user.is_authenticated():
        neww= News.objects.all
        cont = Context({'NewsText':neww})
        return render_to_response('control/news.html', cont, context_instance = RequestContext(request))


def DelNews(request, newwid):
    if request.user.is_authenticated():
        neww = News.objects.get(id=newwid).delete() 
        return redirect('/control/news/')