from django.contrib import admin
from userapp.models import prac, prac1

# Register your models here.
class sadmin(admin.ModelAdmin):
    list_display = ['name','prac_id','add','edu']
admin.site.register(prac,sadmin)


class vadmin(admin.ModelAdmin):
    list_display = ['name','prac1_id','add','edu','phone']
admin.site.register(prac1,vadmin)

