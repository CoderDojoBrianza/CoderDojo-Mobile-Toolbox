from django import forms
from django.utils.translation import ugettext_lazy as _

class TutorialUploadForm(forms.Form):
    tutorial_description = forms.CharField(label='Project Description', max_length=200, widget=forms.Textarea)
    tutorial_file = forms.FileField(max_length=100)

class LevelSelectionForm(forms.Form):
    # This form requires translation, according to doc the solution is to use ugettext_lazy
    LEVEL_ALL = '0'
    LEVEL_BEGINNER = '1'
    LEVEL_INTERMEDIATE = '2'
    LEVEL_ADVANCED = '3'
    LEVEL_CHOICES = (
        (LEVEL_ALL, _('LEVEL_ALL')),
        (LEVEL_BEGINNER, _('LEVEL_BEGINNER')),
        (LEVEL_INTERMEDIATE, _('LEVEL_INTERMEDIATE')),
        (LEVEL_ADVANCED, _('LEVEL_ADVANCED')),
    )
    level = forms.ChoiceField(label=_('Level'),choices=LEVEL_CHOICES)