from django.shortcuts import render
from rest_framework import viewsets

from nestedCrud.models import Song, Singer
from nestedCrud.serializers import SongSerializer, SingerSerializer


# Create your views here.
class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def get_queryset(self):
        return Song.objects.all()

class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

    def get_queryset(self):
        return Singer.objects.all()