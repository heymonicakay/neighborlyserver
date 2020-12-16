"""
Neighborly URL Configuration
"""
from django.conf.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from neighborlyapi.models import *
from neighborlyapi.views import *

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', User, 'user')


urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

