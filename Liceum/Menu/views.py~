# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

from Menu.models import Menu
from Page.models import Page


def EdPgOut(request,pageid):	
    menulist = Menu.objects.filter(visible = True).order_by('number')
    pagelist = Page.objects.get(id = pageid)
    return render_to_response('editpage.html', {'MenuText':menulist, 'Page':pagelist}, context_instance = RequestContext(request))

def MenuOut(request):	
    menulist = Menu.objects.filter(visible = True).order_by('number')
    pagelist = Page.objects.filter(visible = True).order_by('position') 
    temp = loader.get_template('menu.html')
    cont = Context({'MenuText':menulist, 'Pgs':pagelist})
    return HttpResponse(temp.render(cont))
    
def MenuToAdd(request):	
    menulist = Menu.objects.filter(visible = True).order_by('number')
    return render_to_response('add_form.html', {'MenuText':menulist}, context_instance = RequestContext(request))