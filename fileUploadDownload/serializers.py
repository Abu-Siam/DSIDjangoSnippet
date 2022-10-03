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

    def validate(self, attrs):
        count = FileTempStorage.objects.all().count()
        if count  > 0:
            raise serializers.ValidationError("Only one file can be uploaded at a time")
        return attrs