from django.db import models
from datetime import date

# Create your models here.
class Services(models.Model):
    scode = models.CharField(max_length=50, unique = True)
    sname = models.CharField(max_length=50)
    sprice = models.CharField(max_length=50)
    stype = models.CharField(max_length=50)
    screated = models.DateTimeField( auto_now_add=True)
    screated_by = models.CharField(null=True,max_length=50)

    def __str__(self):
        return self.sname

    def screated_at(self):
        return self.screated.strftime('%d %B, %Y')


    class Meta:
        db_table = "Service"
