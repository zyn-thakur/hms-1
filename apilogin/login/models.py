# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.utils.translation import ugettext_lazy as lazy

# # Create your models here.
# class User(AbstractUser):
#     username = models.CharField(max_length=10,unique=true)
#     email = models.EmailField('email address')
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email','first_name','last_name']

#     def __str__(self):
#         return"{}".format(self.email)