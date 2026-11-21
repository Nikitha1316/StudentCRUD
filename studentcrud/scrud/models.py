from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField()
    email=models.EmailField()
    batch=models.CharField(max_length=100)
    photo=models.ImageField(upload_to="student_img")
