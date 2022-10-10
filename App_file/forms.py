from django import forms
from .models import Appfile

class AppfileForm(forms.ModelForm):
    class Meta:
        model = Appfile
        fields = ('tital','files')