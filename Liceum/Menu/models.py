from django.db import models
from django.contrib import admin

# Create your models here.

class Menu(models.Model):
	number = models.IntegerField()
	text = models.CharField(max_length = 30)
	visible = models.BooleanField()
	

class MenuAdmin(admin.ModelAdmin):
    list_display = ('text','visible')


admin.site.register(Menu, MenuAdmin)
