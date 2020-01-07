from django.urls import path,include
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from django.contrib import admin
from . import api

from django.conf import settings

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['token'] = str(refresh.access_token)

        # Add extra responses here
        data['username'] = self.user.username
        data['groups'] = self.user.groups.values_list('name', flat=True)
        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

urlpatterns = [
    # Your URLs...
    path("admin/services/", include("services.urls")),
    path("admin/patients/", include("patients.urls")),
    path("admin/doctors/", include("doctor.urls")),
    path("admin/userdetail/", include("userdetail.urls")),
    path('api/v1/', include(api.router.urls)),
    path('auth/login',MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh',TokenRefreshView.as_view(), name='token_refresh'),
    path('',include('login.urls')),
    path('api-auth/',include('rest_framework.urls'))
] 