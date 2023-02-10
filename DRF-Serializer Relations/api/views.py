from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *
from rest_framework import viewsets

class SingerViewset(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    
class SongViewset(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
