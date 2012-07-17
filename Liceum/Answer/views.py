# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from datetime import datetime
from django.core.mail import send_mail


from Comments.models import Comment
from Answer.models import Answer


def AnsToAdd(request, comid):
    if request.user.is_authenticated():	
        return render_to_response('control/answer/add.html', {'comid':comid}, context_instance = RequestContext(request))

def AddAns(request, comid):
    if request.user.is_authenticated():
        if request.POST['visible'] == "True":
            vis = True
        else:
            vis = False
        ans = Answer(text = request.POST['txt'], name = request.POST['name'], visible = vis, author = request.POST['author'], parent = Comment.objects.get(id = comid))
        ans.save()
        #send_mail('Your comment answered', '', 'from@example.com',['to@example.com'], fail_silently=False)
        #FIXIT
        return redirect('/control/comments/'+ans.parent.thread+'/')

#haz
def DelAns(request, comid):
    if request.user.is_authenticated():
        comm = Comment.objects.get(id=comid) 
        whom = comm.thread
        for ans in Answer.objects.filter(parent=comm):
            ans.delete()
        return redirect('/../../control/comments/'+whom+'/')
 
#haz   
def AnsToEdit(request, comid):
    if request.user.is_authenticated():	
        comm = Comment.objects.get(id=comid) 
        whom = comm.thread
        ans = Answer.objects.get(parent=comm)
        return render_to_response('control/answer/edit.html', {'comid':comid, 'ans':ans}, context_instance = RequestContext(request))
  
def EditAns(request, comid):
    if request.user.is_authenticated():	
        comm = Comment.objects.get(id=comid) 
        whom = comm.thread
        ans = Answer.objects.get(parent=comm)
        if request.POST['visible'] == "True":
            vis = True
        else:
            vis = False
        ans.text = request.POST['txt']
        ans.name = request.POST['name']
        ans.visible = vis
        ans.author = request.POST['author']
        ans.save()
        #send_mail('Your comment answered', '', 'from@example.com',['to@example.com'], fail_silently=False)
        return redirect('/control/comments/'+whom+'/')  