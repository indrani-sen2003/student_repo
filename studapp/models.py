from django.db import models

class stud(models.Model):
	roll=models.IntegerField(primary_key=True)
	sname=models.CharField(max_length=30)
	dob=models.DateField()

class course(models.Model):
    course_code=models.IntegerField(primary_key=True)
    course_name=models.CharField(max_length=30)

# Create your models here.
