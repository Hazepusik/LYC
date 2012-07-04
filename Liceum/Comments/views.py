# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from datetime import datetime

from Comments.models import Comment
from Menu.models import Menu
from Answer.models import Answer

def CommToAdd(request, whom):	
    return render_to_response('addcomment.html', {'whom':whom}, context_instance = RequestContext(request))

def AddComm(request, whom):
    if request.POST['visible'] == "True":
        vis = True
    else:
        vis = False
    comm = Comment(text = request.POST['txt'], name = request.POST['name'], visible = vis, author = request.POST['author'], mailback = request.POST['mail'], thread = whom)
    comm.save()
    #FIXIT
    return redirect('/comments/'+whom+'/')

def DelComm(request, comid):
    Comment.objects.filter(id=comid).delete()
    #FIXIT
    return redirect('/comments/'+whom+'/')

def CommOut(reqest, whom):
    comm = Comment.objects.filter(thread = whom).filter(visible = True).order_by('dateadd')
    ans = Answer.objects.filter(visible = True)
    temp = loader.get_template('comments.html')
    cont = Context({'comments':comm, 'answers':ans})
    return HttpResponse(temp.render(cont))
    