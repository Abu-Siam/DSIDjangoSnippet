from json import loads, dumps

from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from fileUploadDownload.forms import FileDetailsForm
from fileUploadDownload.serializers import FileDetailsSetializer, FileTempStorageSerializer
from fileUploadDownload.models import FileDetailsModel, FileTempStorage
from rest_framework.response import Response

from django.template import RequestContext

# Create your views here.
class fileUploadDownloadView(APIView):
    def get(self, request):
        fm= FileDetailsForm()
        # user = User.objects.cre
        return render(request, 'fileUploadDownload.html', {'form':fm})

    # def post(self, request):
    #     fm= FileDetailsForm(request.POST,request.FILES)
    #     if fm.is_valid():
    #         data = {}
    #         data['name'] =fm.cleaned_data['name']
    #         data['owner'] =fm.cleaned_data['owner']
    #         data['pdf'] =fm.cleaned_data['pdf']
    #         data['cover'] =fm.cleaned_data['cover']
    #         serializer = FileDetailsSetializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #         print(data)
    #     # file = request.FILES['file']
    #     # fs = FileSystemStorage()
    #     # fs.save(file.name, file)
    #     return render(request, 'fileUploadDownload.html', {'form':fm})
    def post(self, request):
        if request.method == 'POST':
            data = {}
            data['name'] = request.POST['filename']
            data['owner'] = request.POST['owner']
            # print(type(FileTempStorage.objects.all().first()))
            # pdf = FileTempStorage.objects.all().first()
            # serializer = FileTempStorageSerializer(pdf)
            # data['pdf'] = serializer.data['pdf']
            # data['pdf'] = ''
            data['cover'] = request.FILES['cover']
            # data['pdf'] = request.FILES['pdf']
            serializer = FileDetailsSetializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            print(data)
        # file = request.FILES['file']
        # fs = FileSystemStorage()
        # fs.save(file.name, file)
        return render(request, 'fileUploadDownload.html')


class fileDownloadView(APIView):
    def get(self, request):
        fileInfos = FileDetailsModel.objects.all()
        serializer = FileDetailsSetializer(fileInfos, many=True)
        # serializer.is_valid(raise_exception=True)
        context = {'files':loads(dumps(serializer.data))}
        print(context)
        return render(request, 'fileDownloadView.html',context)

    def post(self, request):
        return render(request, 'fileDownloadView.html')

class fileUploadTempStorageView(APIView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(fileUploadTempStorageView, self).dispatch(request, *args, **kwargs)
    def get(self, request):
        return render(request,'fileUploadDownload.html')

    def post(self, request):
        data = {}
        data['pdf'] = request.FILES['file']
        serializer = FileTempStorageSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print('ok')
        return Response({'msg':'this is home'},status=HTTP_200_OK)