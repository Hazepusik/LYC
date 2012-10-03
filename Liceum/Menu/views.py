# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

from Menu.models import Menu
from Page.models import Page
from News.models import News
from Storage.models import StorageCell


def EdPgOut(request,pageid):	
    if request.user.is_authenticated():
        menulist = Menu.objects.order_by('number')
        pagelist = Page.objects.get(id = pageid)
        files = StorageCell.objects.filter(page = pagelist).order_by('id')
        return render_to_response('control/page/edit.html', {'MenuText':menulist, 'Page':pagelist, 'Files':files}, context_instance = RequestContext(request))

def MenuOut(request):	
    menulist = Menu.objects.filter(visible = True).exclude(text = 'left').order_by('number')
    pagelist = Page.objects.filter(visible = True).order_by('position') 
  #  if request.user.is_authenticated():
   #     menulist = Menu.objects.order_by('number')
    #    pagelist = Page.objects.order_by('position') 
    leftmenu = Menu.objects.filter(text='left') # gettin' left menu
    leftpages = Page.objects.filter(visible=True).filter(menupoint=leftmenu)
    
    newslist= News.objects.filter(visible = True).order_by('-dateadd')[:3]
    temp = loader.get_template('index.html')
    cont = Context({'MenuText':menulist, 'Pgs':pagelist,'leftmenu':leftpages, 'newosti':newslist})
    return HttpResponse(temp.render(cont))
 
def SubmenuOut(request, menupoint):	
    menupointer = Menu.objects.get(id = menupoint)
    if menupointer.visible == True:
		menulist = Menu.objects.filter(visible = True).exclude(text = 'left').order_by('number')
		pagelist = Page.objects.filter(menupoint = menupointer).filter(visible = True).order_by('position')

		leftmenu = Menu.objects.filter(text='left') # gettin' left menu
		leftpages = Page.objects.filter(visible=True).filter(menupoint=leftmenu)

		newslist= News.objects.filter(visible = True).order_by('-dateadd')[:3]
		temp = loader.get_template('index.html')
		cont = Context({'MenuText':menulist, 'currentmenu':pagelist,'leftmenu':leftpages, 'newosti':newslist, 'nowmenu': menupointer})
		return HttpResponse(temp.render(cont)) 

    
def PgMenuToAdd(request):	
    if request.user.is_authenticated():
        menulist = Menu.objects.order_by('number')
        return render_to_response('control/page/add.html', {'MenuText':menulist}, context_instance = RequestContext(request))

def MenuToAdd(request):	
    if request.user.is_authenticated():
        return render_to_response('control/menu/add.html', {}, context_instance = RequestContext(request))

def AddMenu(request):
    if request.user.is_authenticated():
        if request.POST['visible'] == "True":
            vis = True
        else:
            vis = False
        newmenu = Menu(text = request.POST['menuname'], visible = vis, number = request.POST['pos'])
        newmenu.save()
        return redirect('/control/menu/')
    
def EdMenuOut(request, menuid):	
    if request.user.is_authenticated():
        menulist = Menu.objects.get(id = menuid)
        return render_to_response('control/menu/edit.html', {'Menu':menulist}, context_instance = RequestContext(request))


def EditMenu(request, menuid):
    if request.user.is_authenticated():
        menu = Menu.objects.get(id = menuid)
        menu.text = request.POST['menuname']
        if request.POST['vis'] == "True":
            menu.visible = True
        else:
            menu.visible = False
        menu.number = request.POST['pos']
        menu.save()
        return redirect('/control/menu/')
    
def DelMenu(request, menuid):
    if request.user.is_authenticated():
        neww = Menu.objects.get(id=menuid).delete() 
        return redirect('/control/menu/')
    
    
def ContrMenuOut(request):    
    if request.user.is_authenticated():
        menu= Menu.objects.all
        cont = Context({'MenuText':menu})
        return render_to_response('control/menu.html', cont, context_instance = RequestContext(request))
