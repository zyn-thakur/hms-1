from rest_framework import serializers
from . import models

class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Patients
        fields = "__all__"
        
