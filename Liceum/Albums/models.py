from django.db import models
from django.contrib import admin

class Album(models.Model):
	name = models.CharField(max_length=45)
	text = models.CharField(max_length=150, blank=True)
	visible = models.BooleanField()
	date = models.DateField(auto_now_add=True)
	def __unicode__(self):
		return u'%s %s' % (self.name, self.visible)
	
class ALbumAdmin(admin.ModelAdmin):
    list_display = ('name','visible')

admin.site.register(Album, ALbumAdmin)
