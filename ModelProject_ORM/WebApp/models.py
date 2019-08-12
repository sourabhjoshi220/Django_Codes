from django.db import models

# Create your models here.
class Students(models.Model):
    StdId=models.IntegerField()
    StdName=models.CharField(max_length=30)
    StdMarks=models.FloatField()
    StdAdd=models.CharField(max_length=30)
