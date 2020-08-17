from django import forms
from django.forms import ModelForm

class FormularioEstado(forms.Form):

    estado1=forms.BooleanField(required=False)
    estado2=forms.BooleanField(required=False)
    estado3=forms.BooleanField(required=False)
