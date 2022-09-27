from rest_framework import serializers

from fileUploadDownload.models import FileDetailsModel
class FileDetailsSetializer(serializers.ModelSerializer):
    class Meta:
        model = FileDetailsModel
        fields = ['name','owner','pdf','cover']