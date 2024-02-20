"""
URL configuration for messaging_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from messaging_app.views import *


router = DefaultRouter()
router.register(r'all_messages', AllMessageViewSet, basename='all_messages')
router.register(r'unread_messages', UnreadMessageViewSet, basename='unread_messages')
#router.register(r'read_message', ReadMessageViewSet, basename='read_message')
#router.register(r'delete_message', DeleteMessageViewSet, basename='delete_message')
router.register(r'message', MessageViewSet, basename='message')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]
