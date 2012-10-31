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
    comm = Comment.objects.filter(thread = whom).filter(visible = True).order_by('-dateadd')
    ans = Answer.objects.filter(visible = True)
    dir=False
    zav=False
    all=False
    if whom=='dir':
        dir = True
    elif whom=='zav':
        zav = True
    elif whom=='all':
        all = True
    else:
        return 'Thar id error! You are doing something wrong!'
    return render_to_response('guestbook.html', {'whom':whom, 'comments':comm, 'answers':ans,'dir':dir,'zav':zav,'all':all}, context_instance = RequestContext(request))

def AddComm(request, whom):
    comm = Comment(text = request.POST['txt'], name = request.POST['name'], visible = False, author = request.POST['author'], mailback = request.POST['mail'], thread = whom)
    comm.save()
    return redirect('/addcomment/'+whom+'/')

def DelComm(request, comid):
    if request.user.is_authenticated():
        comm = Comment.objects.get(id=comid) 
        whom = comm.thread
       # ans = Answer.objects.get(parent=comm)
        for ans in Answer.objects.filter(parent=comm):
            ans.delete()
        comm.delete()
        return redirect('/../../control/comments/'+whom+'/')


def CommOut(reqest, whom):
    comm = Comment.objects.filter(thread = whom).filter(visible = True).order_by('dateadd')
    ans = Answer.objects.filter(visible = True)
    temp = loader.get_template('comments.html')
    cont = Context({'comments':comm, 'answers':ans})
    return HttpResponse(temp.render(cont))


def ContrCommOut(request, whom):
    if request.user.is_authenticated():
        comm = Comment.objects.filter(thread = whom).order_by('dateadd')
        ans = Answer.objects.all()
        cont = Context({'comments':comm, 'answers':ans, 'isans':False})
        return render_to_response('control/comments.html', cont, context_instance = RequestContext(request))
    
