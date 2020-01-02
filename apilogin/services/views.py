from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from .models import Services
from rest_framework import response
# from rest_framework.decorators import action
# from rest_framework import parsers

# Create your views here.
class ServicesViewset(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = serializers.ServicesSerializer
