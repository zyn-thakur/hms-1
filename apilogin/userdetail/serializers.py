from rest_framework import serializers
from . import models

class UserdetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Userdetail
        fields = "__all__"
        
