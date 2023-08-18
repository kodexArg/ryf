from django.shortcuts import render
from rest_framework import generics
from api.models import Settings
from api.serializers import SettingsSerializer

class SettingsListCreateView(generics.ListCreateAPIView):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer
