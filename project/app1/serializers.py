from rest_framework import serializers
from .models import PersonalInfo

class PersonalInfoSerilaizer(serializers.ModelSerializer):

    class Meta:
        model = PersonalInfo
        fields ='__all__'