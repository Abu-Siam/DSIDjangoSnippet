from django.shortcuts import render
from rest_framework.views import APIView
from fileUploadDownload.forms import FileDetailsForm
from fileUploadDownload.serializers import FileDetailsSetializer
from django.template import RequestContext

# Create your views here.
class fileUploadDownloadView(APIView):
    def get(self, request):
        fm= FileDetailsForm()
        return render(request, 'fileUploadDownload.html', {'form':fm})

    def post(self, request):
        fm= FileDetailsForm(request.POST,request.FILES)
        if fm.is_valid():
            data = {}
            data['name'] =fm.cleaned_data['name']
            data['owner'] =fm.cleaned_data['owner']
            data['pdf'] =fm.cleaned_data['pdf']
            data['cover'] =fm.cleaned_data['cover']
            serializer = FileDetailsSetializer(data=data)
            if serializer.is_valid():
                serializer.save()
            print(data)
        # file = request.FILES['file']
        # fs = FileSystemStorage()
        # fs.save(file.name, file)
        return render(request, 'fileUploadDownload.html', {'form':fm})

