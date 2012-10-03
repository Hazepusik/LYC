# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

from Page.models import Page
from Menu.models import Menu
from Storage.models import StorageCell
#optimization and algorithmization

def PageOut(request,pageid):	
    pg = Page.objects.filter(visible = True).get(id = pageid)
    menulist = Menu.objects.filter(visible = True).exclude(text = 'left').order_by('number')
    curmenu = pg.menupoint
    pagelist = Page.objects.filter(menupoint = curmenu).filter(visible = True).order_by('position') 
    files = StorageCell.objects.filter(visible = True).filter(page = pg)
    temp = loader.get_template('content.html')
    cont = Context({'Page':pg, 'Files': files, 'MenuText':menulist, 'currentmenu':pagelist,'nowmenu':curmenu})
    return HttpResponse(temp.render(cont))

def AddPage(request):
    if request.user.is_authenticated():
        if request.POST['visible'] == "True":
            vis = True
        else:
            vis = False
        newpage = Page(name = request.POST['pgname'], menupoint = Menu.objects.get(id = request.POST['list']), text =  request.POST['txt'], visible = vis, title = request.POST['header'], position = request.POST['pos'])
        newpage.save()
        return redirect('/Pages/'+str(newpage.id))
    
def EditPage(request,pageid):
    if request.user.is_authenticated():
        page = Page.objects.get(id = pageid)
        page.name = request.POST['pgname']
        page.menupoint = Menu.objects.get(id = request.POST['list'])
        page.text =  request.POST['txt']
        page.visible = request.POST['visible']
        page.title = request.POST['header'] 
        page.position = request.POST['pos']
        page.save()
        return redirect('/Pages/'+str(page.id))
