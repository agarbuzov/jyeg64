from django import forms


class JSONForm(forms.Form):
    text = forms.CharField()
