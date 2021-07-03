from django import forms

class QuestionForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email_address = forms.CharField(max_length=100)
    message = forms.Textarea()
