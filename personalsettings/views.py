from django.shortcuts import render

from rest_framework import generics
from rest_framework import permissions

from personalsettings.models import PublicProfile, AccountSettings
from personalsettings.serializers import PublicProfileSerializer, AccountSettingsSerializer
from personalsettings.permissions import IsOwner


class PublicProfileView(generics.ListCreateAPIView):
    serializer_class = PublicProfileSerializer
    queryset = PublicProfile.objects.all().order_by("-updated_at")
    permission_classes = (IsOwner, permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class PublicProfileUpdateView(generics.UpdateAPIView):
    serializer_class = PublicProfileSerializer
    queryset = PublicProfile.objects.all().order_by("updated_at")
    permission_classes = (IsOwner, permissions.IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
