from django.shortcuts import render
from rest_framework.views import APIView
from fileUploadDownload.forms import FileDetailsForm

# Create your views here.
class fileUploadDownloadView(APIView):
    def get(self, request):
        fm= FileDetailsForm()
        return render(request, 'fileUploadDownload.html', {'form':fm})

    def post(self, request):
        # file = request.FILES['file']
        # fs = FileSystemStorage()
        # fs.save(file.name, file)
        return render(request, 'fileUploadDownload/fileUploadDownload.html')