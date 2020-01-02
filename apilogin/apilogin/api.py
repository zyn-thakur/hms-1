from rest_framework import routers
from services.views import ServicesViewset
from patients.views import PatientsViewset



router = routers.DefaultRouter()
router.register(r'services', ServicesViewset)
router.register(r'patients', PatientsViewset)