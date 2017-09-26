from .account.views import ProfileViewSet

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'profile', ProfileViewSet, base_name='profile')

urlpatterns = [
    url(r'^', include(router.urls)),
]