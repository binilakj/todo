from . models import Work
from django import forms

class WorkForm(forms.ModelForm):
    class Meta:
        model=Work
        fields=['name','priority','date']