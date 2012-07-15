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
    return render_to_response('control/answer/add.html', {'comid':comid}, context_instance = RequestContext(request))

def AddAns(request, comid):
    if request.POST['visible'] == "True":
        vis = True
    else:
        vis = False
    ans = Answer(text = request.POST['txt'], name = request.POST['name'], visible = vis, author = request.POST['author'], parent = Comment.objects.get(id = comid))
    ans.save()
    #send_mail('Your comment answered', '', 'from@example.com',['to@example.com'], fail_silently=False)
    #FIXIT
    return redirect('/comments/'+ans.parent.thread+'/')
