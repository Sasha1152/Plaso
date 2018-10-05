from django.contrib import admin
from . models import *

class BoardAdmin(admin.ModelAdmin):
	fields = ['name', 'descriptions']

admin.site.register(Board)