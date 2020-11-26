from django.db import models

class stud(models.Model):
	roll=models.IntegerField(primary_key=True)
	sname=models.CharField(max_length=30)
	dob=models.DateField()
    
# Create your models here.
