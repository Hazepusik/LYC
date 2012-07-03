from django.db import models
from django.contrib import admin
from Comments.models import Comment

class Answer(models.Model):
	parent = models.ForeignKey(Comment, null=True, blank=True)
	dateadd = models.DateTimeField(auto_now_add=True)
	author = models.CharField(max_length=30)
	name = models.CharField(max_length=45)
	text = models.TextField(null=True,blank=True)
	visible = models.BooleanField()

class AnswerAdmin(admin.ModelAdmin):
	list_display = ('name','author','dateadd')
	
admin.site.register(Answer, AnswerAdmin) 
