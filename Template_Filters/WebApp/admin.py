from django.contrib import admin
from WebApp.models import FilterModel

class FilterModelAdmin(admin.ModelAdmin):
    list_display = ['name','subject','dept','date']
admin.site.register(FilterModel,FilterModelAdmin)