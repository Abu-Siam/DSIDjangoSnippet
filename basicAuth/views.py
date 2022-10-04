from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

from basicAuth.customAuthentication import CustomAuthentication
from basicAuth.customPermission import MyPermission
from basicAuth.customThrottle import MyUserRateThrottle
from basicAuth.models import Student
from basicAuth.serializer import StudentSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, \
    DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, DjangoObjectPermissions


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    # queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]  # we can add permission and authentication in rest framework config in settings for all api
    # permission_classes= [AllowAny] # for all api
    # permission_classes = [IsAdminUser]  # for admin user


    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]  # we can add permission and authentication in rest framework config in settings for all api
    # permission_classes = [IsAuthenticatedOrReadOnly]  # for all api
    # permission_classes = [DjangoModelPermissions]  # for all api
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]  # for all api
    # permission_classes = [DjangoObjectPermissions]  # for all api
    # permission_classes = [MyPermission]  # for all api


    # authentication_classes = [TokenAuthentication]
    authentication_classes = [CustomAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = '__all__'
    search_fields = ['^name','=city']

    # throttle_classes = [AnonRateThrottle, MyUserRateThrottle] #for custom throttle use scopedthrottle

    def get_queryset(self):
        return Student.objects.all()

