from django.db import models
from django.contrib import admin
from Menu.models import Menu

class Page(models.Model):
	name = models.CharField(max_length=30)
	text = models.TextField(null=True,blank=True)
	visible = models.BooleanField()
	menupoint = models.ForeignKey(Menu,on_delete=models.SET_NULL, null=True)
	title = models.CharField(null=True,blank=True,max_length=30)
	position = models.IntegerField(null=True,blank=True)
	innerpage = models.BooleanField()
	
	def __unicode__(self):
		return u'%s %s' % (self.name, self.visible)
	
class PageAdmin(admin.ModelAdmin):
    list_display = ('name','visible')

admin.site.register(Page, PageAdmin)
