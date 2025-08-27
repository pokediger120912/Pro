from django import forms
from .models import Mod

class ModForm(forms.ModelForm):
    class Meta:
        model = Mod
        fields = ['title', 'description', 'file']
