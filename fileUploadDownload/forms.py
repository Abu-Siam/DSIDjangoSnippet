from django import forms
from fileUploadDownload.models import FileDetailsModel

class FileDetailsForm(forms.ModelForm):
    class Meta:
        model = FileDetailsModel
        fields = ['name','owner','pdf','cover']


