
from django import forms

from bio.models import Bio, Link


class BioForm(forms.ModelForm):
    class Meta:
        model = Bio
        fields = ('full_name', 'surname', 'image', 'birthday', 'nationality', 'gender',
        'degree', 'academic_title', 'college', 'department', 'major', 'specialty',
        'position', 'occupation', 'mother_lang', 'other_langs', 'personal_email',
        'work_email',

        'ar_full_name', 'ar_nationality', 'ar_academic_title', 'ar_college',
        'ar_department', 'ar_major', 'ar_specialty', 'ar_position', 'ar_occupation',
        'ar_state', 'ar_district', 'ar_hiring_date', 'ar_direct_date',
        'ar_mother_lang', 'ar_other_langs',)


class DeleteBioForm(forms.ModelForm):
    class Meta:
        model = Bio
        fields = ()


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('url',)


class DeleteLinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ()

