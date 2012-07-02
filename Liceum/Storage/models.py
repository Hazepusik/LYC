from django.db import models
from django.contrib import admin
from Page.models import Page

# Create your models here.
class StorageCell(models.Model):
	name = models.CharField(max_length=45)
	filetype = models.CharField(max_length=5)
	page = models.ForeignKey(Page,on_delete=models.SET_NULL, null=True)
	subj = models.FileField(upload_to="media/", blank=True)
	visible = models.BooleanField()
	
class StorageCellAdmin(admin.ModelAdmin):
    list_display = ('name','visible')

admin.site.register(StorageCell, StorageCellAdmin)
