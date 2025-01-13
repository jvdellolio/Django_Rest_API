from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonalInfoViewSet

router = DefaultRouter()
router.register(r'personalinfo', PersonalInfoViewSet)


urlpatterns = [
    path('', include(router.urls)),
]