
from django import forms

from settings.models import Settings


class SettingsForm(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ('image',)

