from rest_framework.routers import DefaultRouter
from django.urls import re_path, path
from django.urls import include
# from rest_framework.authtoken import views

from .views import PostingViewSet, ClientViewSet, MessageViewSet


router_v1 = DefaultRouter()
router_v1.register('posts', PostingViewSet)
router_v1.register('clients', ClientViewSet)
router_v1.register('message', MessageViewSet, basename='message')


urlpatterns = [
    re_path('^v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),

]
