from django.contrib import admin
from WebApp.models import Students
# Register your models here.
class StdAdmin(admin.ModelAdmin):
    list_display = ['id','StdId','StdName','StdMarks','StdAdd']
admin.site.register(Students,StdAdmin)