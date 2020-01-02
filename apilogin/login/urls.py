from django.urls import path
# from myapi.core import views
from . import  views
urlpatterns = [
    path('', views.show, name='show'),
]