from django import forms

class TutorialUploadForm(forms.Form):
    tutorial_description = forms.CharField(label='Project Description', max_length=200, widget=forms.Textarea)
    tutorial_file = forms.FileField(max_length=100)