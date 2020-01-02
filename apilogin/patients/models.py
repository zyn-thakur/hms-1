from django.db import models
from datetime import date
from services.models import Services
# from multiselectfield import MultiSelectField

# Create your models here.
class Patients(models.Model):
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    OTHER = 'OTHER'

    SEX_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]

    pcode = models.CharField(max_length=50, unique = True)
    pname = models.CharField(max_length=50)
    page = models.IntegerField()
    psex = models.CharField(max_length=6,choices = SEX_CHOICES,default = MALE)
    paddress = models.CharField(max_length=100)
    pphone = models.CharField(max_length=15,blank=True)
    pcreated_by = models.CharField(null=True,max_length=50)
    pcreated_at = models.DateTimeField(auto_now_add=True)
    referred_by = models.CharField(max_length=50,null=True,blank = True)
    services = models.ManyToManyField(Services)

    def __str__(self):
        return self.pname

    def ppcreated_at(self):
        return self.pcreated_at.strftime('%d %B, %Y')




    class Meta:
        db_table = "Patient"
        ordering = ["-pcreated_at"]
