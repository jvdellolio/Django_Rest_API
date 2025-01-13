from rest_framework import viewsets
from .models import PersonalInfo
from .serializers import PersonalInfoSerilaizer

class PersonalInfoViewSet(viewsets.ModelViewSet):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerilaizer