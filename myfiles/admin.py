from django.contrib import admin
from myfiles.models import Teacher

# Register your models here.

class AdminT(admin.ModelAdmin):
    list_display = ['id','name','last_name','age']

admin.site.register(Teacher,AdminT)