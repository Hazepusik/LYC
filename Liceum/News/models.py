from django.db import models
from django.contrib import admin

# Create your models here.
class News(models.Model):
	name = models.CharField(max_length=45)
	text = models.TextField(null=True,blank=True)
	visible = models.BooleanField()
	dateadd = models.DateField()

class NewsAdmin(admin.ModelAdmin):
    list_display = ('name','dateadd') 

admin.site.register(News, NewsAdmin)
