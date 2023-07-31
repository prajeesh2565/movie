from django import forms
from . models import *

class MovieForm(forms.ModelForm):
    class Meta:
        model=movies
        fields=['name','img','desc','year']