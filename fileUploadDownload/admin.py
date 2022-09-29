from django.contrib import admin
from fileUploadDownload.models import FileDetailsModel,FileTempStorage
# Register your models here.
admin.site.register(FileDetailsModel)
admin.site.register(FileTempStorage)