from django.db import models


# Create your models here.
class Userdetail(models.Model):
    username =  models.CharField(max_length=200)
    uname = models.CharField(max_length=200)
    urole = models.CharField(max_length=200)
    uemail = models.EmailField()

    def __str__(self):
        return self.username

    class Meta:
        db_table = "Userdetail"

