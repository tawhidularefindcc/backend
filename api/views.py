from rest_framework import viewsets
from django.shortcuts import render
from .models import Profiles
from .serializers import ProfilesSerializer

class ProfileView(viewsets.ModelViewSet):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer
