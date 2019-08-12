from django import forms
class EmpForm(forms.Form):
    Name=forms.CharField()
    Salary=forms.IntegerField()
    Bot_Field=forms.CharField(required=False,widget=forms.HiddenInput)
    def clean(self):
        print("Welcome to BOT Validations")
        Cdata=super().clean()
        bhandel=Cdata['Bot_Field']
        if len(bhandel)>0:
            raise forms.ValidationError("Sorry Bot")
