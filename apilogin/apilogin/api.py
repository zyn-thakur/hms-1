from rest_framework import routers
from services.views import ServicesViewset
from patients.views import PatientsViewset
from doctor.views import DoctorsViewset
from userdetail.views import UserdetailViewset





router = routers.DefaultRouter()
router.register(r'services', ServicesViewset)
router.register(r'patients', PatientsViewset)
router.register(r'doctors', DoctorsViewset)
router.register(r'userdetail', UserdetailViewset)