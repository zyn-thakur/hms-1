from django.db import models
from datetime import date


# Create your models here.
class Doctors(models.Model):
    dcode = models.CharField(max_length=50, unique = True)
    dname = models.CharField(max_length=50)
    ddepart = models.CharField(max_length=50)
    dnmc = models.CharField(max_length=50)
    dphone = models.CharField(max_length=15,blank=True)
    demail = models.EmailField()
    dcreated = models.DateTimeField( auto_now_add=True)
    dcreated_by = models.CharField(null=True,max_length=50)
    def __str__(self):
        return self.dname

    def dcreated_at(self):
        return self.dcreated.strftime('%d %B, %Y')


    class Meta:
        db_table = "Doctors"
