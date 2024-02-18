
from django import forms

from history.models import Log


class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ()

