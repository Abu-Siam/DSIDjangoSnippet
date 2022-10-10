"""djangoFileUploadDownload URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from basicAuth.auth import CustomAuthToken

from basicAuth.views import StudentViewSet
from nestedCrud.views import SongViewSet, SingerViewSet

router = DefaultRouter()

router.register('studentapi', StudentViewSet, basename='studentapi')
router.register('songapi', SongViewSet, basename='songapi')
router.register('singerapi', SingerViewSet, basename='singerapi')
# router.register('student-detail', StudentViewSet, basename='studentDetail')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fileUploadDownload.urls')),
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('gettoken/',obtain_auth_token),
    path('gettoken2/',CustomAuthToken.as_view()),
    path('student-detail/<int:pk>', StudentViewSet.as_view({'get': 'list'}), name='student-detail'),
    path('song-detail/<int:pk>', SongViewSet.as_view({'get': 'list'}), name='song-detail'),
    path('singer-detail/<int:pk>', SingerViewSet.as_view({'get': 'list'}), name='singer-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
