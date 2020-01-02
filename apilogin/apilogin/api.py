from rest_framework import routers
from services.views import ServicesViewset



router = routers.DefaultRouter()
router.register(r'services', ServicesViewset)