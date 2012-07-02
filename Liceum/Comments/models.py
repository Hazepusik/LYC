from django.db import models
from django.contrib import admin


class Comment(models.Model):
	name = models.CharField(max_length=45)
	text = models.TextField(null=True,blank=True)
	visible = models.BooleanField()
	dateadd = models.DateTimeField(auto_now_add=True)
	author = models.CharField(max_length=15)
	parent = models.ForeignKey('self', null=True, blank=True)
	
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name','author','dateadd')
    
    
admin.site.register(Comment, CommentsAdmin) 
