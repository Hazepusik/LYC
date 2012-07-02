# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

from Menu.models import Menu
from Page.models import Page


def MenuOut(request):	
    menulist = Menu.objects.filter(visible = True).order_by('number')
    pagelist = Page.objects.filter(visible = True).order_by('position')
    temp = loader.get_template('menu.html')
    cont = Context({'MenuText':menulist, 'Pgs':pagelist})
	
    return HttpResponse(temp.render(cont))