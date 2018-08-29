from django import forms
from django.utils.translation import ugettext_lazy as _
# from . models import *


class TutorialUploadForm(forms.Form):
    tutorial_description = forms.CharField(
        label='Project Description',
        max_length=200,
        widget=forms.Textarea
    )
    tutorial_file = forms.FileField(max_length=100)


class LevelSelectionForm(forms.Form):
    # This form requires translation,
    # according to doc the solution is to use ugettext_lazy
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
    level = forms.ChoiceField(label=_('Level'), choices=LEVEL_CHOICES)


# Custom form field for participant
class ParticipantModelChoiceField(forms.ModelChoiceField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def label_from_instance(self, participant):
        return participant.name + " " + participant.surname


class CheckInOutForm(forms.Form):
    participant_id = forms.CharField(
        label=_('Participant_Id'),
        max_length=200,
        required=False
    )
    ticket_id = forms.CharField(
        label=_('Ticket Id'),
        max_length=200,
        required=False
    )
    participant = ParticipantModelChoiceField(
        label=_('Participant'),
        queryset=None,
        required=False
    )  # Here we use a list of participants from the db (we assume it's small!)

    def __init__(self, queryset_for_form=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['participant'].queryset = queryset_for_form

    CHECK_IN = '1'
    CHECK_IN_CANCEL = '0'
    CHECK_CHOICES = (
        (CHECK_IN, _('Check in')),
        (CHECK_IN_CANCEL, _('Cancel check in')),
    )
    check_in_out = forms.ChoiceField(
        label=_('Check_in_or_cancel'),
        choices=CHECK_CHOICES, widget=forms.RadioSelect, initial=CHECK_IN
    )


class RatingForm(forms.Form):
    # Here value is an integer by design
    value = forms.IntegerField(label=_('Rating'), min_value=1, max_value=5)
    rating_author = forms.CharField(
        label=_('Rating_Author'),
        required=False,
        max_length=150,
        strip=True
    )
    comment = forms.CharField(
        label=_('Rating_Comment'),
        max_length=1500,
        required=False,
        strip=True,
        widget=forms.Textarea
    )
