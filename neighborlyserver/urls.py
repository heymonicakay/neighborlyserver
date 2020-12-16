"""neighborlyserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
"""docstrings"""
from django.conf.urls import include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from neighborlyapi.views import register_user, login_user, Users
from neighborlyapi.views import Subscriptions, Posts, Reactions, Comments
from neighborlyapi.views import Tags, PostTags, Categories

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'categories', Categories, 'category')
router.register(r'tags', Tags, 'tag')
router.register(r'comments', Comments, 'comment')
router.register(r'post_tags', PostTags, 'posttag')
router.register(r'posts', Posts, 'post')
router.register(r'users', Users, 'user')
router.register(r'reactions', Reactions, 'reaction')
router.register(r'subscriptions', Subscriptions, 'subscription')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]
urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

