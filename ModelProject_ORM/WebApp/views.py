from django.shortcuts import render
from WebApp.models import Students
from django.http import HttpResponse

# Create your views here.
def Student_View(request):
    StdList=Students.objects.all()
    My_Dict={'slist':StdList}
    return render(request,'MyApp/Welcome.html',My_Dict)