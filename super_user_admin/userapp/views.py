from django.shortcuts import render
from django.http import HttpResponse
from userapp.models import prac
# Create your views here.
def prac_view(request):
    praclist=prac.objects.all()
    print(type(praclist))
    return render(request,"html_files/second.html")

