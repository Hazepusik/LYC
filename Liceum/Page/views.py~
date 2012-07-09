# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

from Page.models import Page
from Menu.models import Menu
#optimization and algorithmization

def PageOut(request,pageid):	
    page = Page.objects.filter(visible = True).get(id = pageid)
 #   if request.user.is_authenticated():
  #      page = Page.objects.get(id = pageid)
    temp = loader.get_template('Pages.html')
    cont = Context({'Page':page})
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