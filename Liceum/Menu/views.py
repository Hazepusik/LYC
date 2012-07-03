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
    
def PgMenuToAdd(request):	
    menulist = Menu.objects.filter(visible = True).order_by('number')
    return render_to_response('addpage.html', {'MenuText':menulist}, context_instance = RequestContext(request))

def MenuToAdd(request):	
    return render_to_response('addmenu.html', {}, context_instance = RequestContext(request))

def AddMenu(request):
    if request.user.is_authenticated():
        newmenu = Menu(text = request.POST['menuname'], visible = request.POST['visible'], number = request.POST['pos'])
        newmenu.save()
        return redirect('/Menus/')