from django.contrib import admin
from .models import Information

class InformationAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'file']



admin.site.register(Information, InformationAdmin)
