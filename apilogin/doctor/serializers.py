from rest_framework import serializers
from . import models

class DoctorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Doctors
        fields = "__all__"
        
