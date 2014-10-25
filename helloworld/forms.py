from django import forms


class ZipcodeForm(forms.Form):
    number = forms.CharField(max_length=7, min_length=7)
