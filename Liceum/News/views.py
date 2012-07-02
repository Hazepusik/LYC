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