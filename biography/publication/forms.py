
from django import forms

from publication.models import Publication


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ( 'title', 'researchers', 'publication_date', 'journal', 'volume', 'issue',
        'pages', 'book', 'publisher', 'description', 'url',)

class DeletePublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ()

