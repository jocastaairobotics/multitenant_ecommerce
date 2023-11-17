from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=10)
    dob = models.DateField()
    bg = models.CharField(max_length=3)
    marks = models.FloatField()
