from rest_framework import routers
from services.views import ServicesViewset
from patients.views import PatientsViewset
from doctor.views import DoctorsViewset
from userdetail.views import UserdetailViewset
from login.views import RegisterViewSet
from login.views import LoginViewSet




router = routers.DefaultRouter()
router.register(r'services', ServicesViewset)
router.register(r'patients', PatientsViewset)
router.register(r'doctors', DoctorsViewset)
router.register(r'userdetail', UserdetailViewset)
router.register(r'register', RegisterViewSet)
router.register(r'login', LoginViewSet)