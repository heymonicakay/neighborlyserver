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
router.register(r'users', Users, 'user')
router.register(r'profileimages', ProfileImages, 'profileimage')
router.register(r'itemimages', ItemImages, 'itemimage')
router.register(r'categories', Categories, 'category')
router.register(r'conditions', Conditions, 'condition')
router.register(r'tags', Tags, 'tag')
router.register(r'itemtags', ItemTags, 'itemtag')
router.register(r'descriptionaccuracys', DescriptionAccuracys, 'descriptionaccuracy')
router.register(r'items', Items, 'item')
router.register(r'messages', Messages, 'message')
router.register(r'reservations', Reservations, 'reservation')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
