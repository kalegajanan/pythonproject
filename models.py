from django.db import models

# Create your models here.
class project(models.Model):
    startdate=models.DateField()
    enddate= models.DateField()
    name=models.CharField(max_length=30)
    assignedto= models.CharField(max_length=30)
    priority = models.IntegerField()
    
