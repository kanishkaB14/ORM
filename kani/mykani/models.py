from django.db import models
from django.contrib import admin
class car_service(models.Model):
 Car_No = models.CharField(max_length=10,primary_key= True)
 Name = models.CharField()
 Car_Model = models.CharField()
 Phone_No = models.IntegerField()
 Address = models.TextField()
 Problem = models.CharField()
 Brand = models.CharField()
class car_serviceAdmin(admin.ModelAdmin):
 list_display = ["Car_No","Name","Car_Model","Phone_No","Address","Problem","Brand"]
# Create your models here.
