from django.shortcuts import render
from WebApp.models import FilterModel
# Create your views here.
def Dataview(request):
    datalist=FilterModel.objects.all()
    return render(request,'MyApp/Welcome.html',{'datalist':datalist})
