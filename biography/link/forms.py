
from django import forms

from link.models import Link


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('url',)


class DeleteLinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ()

