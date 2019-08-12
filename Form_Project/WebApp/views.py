from django.shortcuts import render
from WebApp import forms
# Create your views here.
def EmpView(request):
    form=forms.EmpForm()
    if request.method=='POST':
        form=forms.EmpForm(request.POST)
        if form.is_valid():
            print("Validations are Success Folks....!!")
            print(form.cleaned_data['Name'])
            print(form.cleaned_data['Salary'])

    return render(request, 'MyApp/Welcome.html', {'form': form})