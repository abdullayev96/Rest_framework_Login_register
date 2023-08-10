from django.contrib import admin
from .models import *

#
class SendUserAdmin(admin.ModelAdmin):
    list_display = ['id','reference_number','verification_code','full_name', 'number', 'email', 'address', 'body','status', 'file', 'created']

admin.site.register(SendUser)

