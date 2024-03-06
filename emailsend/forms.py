from django import forms
class email_form(forms.Form):
    #name=forms.CharField(max_length=233)
    email=forms.EmailField()
    subject=forms.CharField(widget=forms.Textarea)
    body=forms.CharField( max_length=255, required=False)