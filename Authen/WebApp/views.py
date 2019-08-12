from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from WebApp.forms import SignUpForm
def Home_Page(request):
    return render(request,'MyApp/Home.html')
@login_required
def Customer(request):
    return render(request,'MyApp/Customer.html')
def Logout_View(request):
    return render(request, 'MyApp/logout.html')
from django.http import HttpResponseRedirect
def Registration_View(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        user=form.save(commit=True)
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, "MyApp/registration.html",{'form':form})