"""bokikun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from account import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, base_name='users')
router.register(r'friends', views.FriendViewSet, base_name='friends')

users_router = routers.NestedSimpleRouter(router, r'users', lookup='owner')
users_router.register(r'holders', views.FakeUserViewSet)

urlpatterns = [
    url(r'^api/access', views.AccessView.as_view()),
    url(r'^api/users/me', views.MeView.as_view()),
    url(r'^api/', include(router.urls)),
    url(r'^api/', include(users_router.urls)),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    url(r'^admin/', admin.site.urls),
]
