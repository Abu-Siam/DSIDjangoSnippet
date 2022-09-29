from django.urls import path

from fileUploadDownload.views import fileUploadDownloadView, fileDownloadView, fileUploadTempStorageView

urlpatterns = [
    path('file-upload/', fileUploadDownloadView.as_view(), name='file-upload'),
    path('file-download-view/', fileDownloadView.as_view(), name='file-download-view'),
    path('file-upload/upload/', fileUploadTempStorageView.as_view(), name='file-upload/upload'),
    ]