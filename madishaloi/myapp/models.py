from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Doctor(models.Model):
    image = models.FileField(blank=True)
    doctor_name = models.CharField(blank=True,max_length=200)
    specialist =  models.CharField(blank=True,max_length=200)
    lacation = models.CharField(blank=True,max_length=100)
    education_background = models.CharField(blank=True,max_length=300)
    phone = models.CharField(blank=True,max_length=50)
    address = models.CharField(blank=True,max_length=300)
    user_reviwe = models.CharField(blank=True,max_length=60)
    description = models.CharField(blank=True,max_length=600)

class Medicine(models.Model):
    name = models.CharField(blank=True,max_length=200)
    image = models.FileField(blank=True)
    company_name = models.CharField(blank=True,max_length=200)
    group_name = models.CharField(blank=True,max_length=200)
    indication = models.CharField(blank=True,max_length=600)
    dose = models.CharField(blank=True,max_length=600)
    side_effect = models.CharField(blank=True,max_length=600)
    type = models.CharField(blank=True,max_length=200)
    price = models.CharField(blank=True,max_length=200)

class Ambulance(models.Model):
    name = models.CharField(blank=True,max_length=200)
    image = models.FileField(blank=True)
    address = models.CharField(blank=True,max_length=200)
    hospital_name = models.CharField(blank=True,max_length=200)
    mobile = models.CharField(blank=True,max_length=200)


#user registation
class author(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_picture=models.FileField()
    details = models.TextField()
    blood_group = models.TextField()
    def __str__(self):
        return self.name.username