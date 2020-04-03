from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProfileSerializer
from .serializers import PromiseSerializer
from .serializers import ProgressSerializer
from .models import Profile
from .models import Promise
from .models import Progress

class ProfileView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

class PromiseView(viewsets.ModelViewSet):
    serializer_class = PromiseSerializer
    queryset = Promise.objects.all()

class ProgressView(viewsets.ModelViewSet):
    serializer_class = ProgressSerializer
    queryset = Progress.objects.all()
