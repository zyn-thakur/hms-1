from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from .models import Doctors
from rest_framework import response
from rest_framework.decorators import action
from rest_framework import parsers

# Create your views here.
class DoctorsViewset(viewsets.ModelViewSet):
    queryset = Doctors.objects.all()
    serializer_class = serializers.DoctorsSerializer
