from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from django.contrib import admin
urlpatterns = [
    # Your URLs...
    path('admin/',admin.site.urls), #admin routes
    path('api/token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(), name='token_refresh'),
    path('',include('login.urls')),
    path('api-auth/',include('rest_framework.urls'))
] 