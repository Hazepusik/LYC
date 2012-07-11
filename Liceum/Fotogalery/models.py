from django.db import models
from Albums.models import Album
from django.contrib import admin

class Foto(models.Model):
	name = models.CharField(max_length=45)
	text = models.CharField(max_length=150)
	album = models.ForeignKey(Album)
	subj = models.ImageField(upload_to="fotogalery/", blank=True)
	visible = models.BooleanField()
	
class FotoAdmin(admin.ModelAdmin):
    list_display = ('name','visible')

admin.site.register(Foto, FotoAdmin)
