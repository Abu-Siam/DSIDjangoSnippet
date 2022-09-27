from django.urls import path

from fileUploadDownload.views import fileUploadDownloadView

urlpatterns = [
    path('file-details/', fileUploadDownloadView.as_view(), name='file-details'),
    ]