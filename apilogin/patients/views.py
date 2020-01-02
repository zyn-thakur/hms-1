from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from .models import Patients
from rest_framework import response
from rest_framework.decorators import action
from rest_framework import parsers

# Create your views here.
class PatientsViewset(viewsets.ModelViewSet):
    queryset = Patients.objects.all()
    serializer_class = serializers.PatientsSerializer
