from django import forms


class ResultForm(forms.Form):
    question = forms.CharField(required=True)
    answer = forms.CharField(required=True)
