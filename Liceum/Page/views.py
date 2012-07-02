# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

from Page.models import Page

def PageOut(request,pageid):	
    page = Page.objects.filter(visible = True).get(id = pageid)
    temp = loader.get_template('Pages.html')
    cont = Context({'Page':page})

    return HttpResponse(temp.render(cont))