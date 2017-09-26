from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import detail_route, list_route

from django.conf import settings

from account.models import Profile

from .serializer import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return self.queryset