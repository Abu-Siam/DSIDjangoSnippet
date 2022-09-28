from django.urls import path

from fileUploadDownload.views import fileUploadDownloadView,fileDownloadView

urlpatterns = [
    path('file-upload/', fileUploadDownloadView.as_view(), name='file-upload'),
    path('file-download-view/', fileDownloadView.as_view(), name='file-download-view'),
    ]