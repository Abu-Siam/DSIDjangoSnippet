from rest_framework import serializers

from fileUploadDownload.models import FileDetailsModel, FileTempStorage


class FileDetailsSetializer(serializers.ModelSerializer):
    class Meta:
        model = FileDetailsModel
        fields = ['name','owner','cover']

class FileTempStorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileTempStorage
        fields = ['pdf']