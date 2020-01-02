from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from django.contrib import admin
from . import api
from django.conf import settings

urlpatterns = [
    # Your URLs...
    path('admin/',admin.site.urls), #admin routes
    path("services/", include("services.urls")),
    path("patients/", include("patients.urls")),
    path('api/v1/', include(api.router.urls)),
    path('api/token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
    path('',include('login.urls')),
    path('api-auth/',include('rest_framework.urls'))
] 