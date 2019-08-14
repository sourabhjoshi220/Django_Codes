from django.db import models

# Create your models here.
class prac(models.Model):
    name=models.CharField(max_length=30)
    prac_id=models.IntegerField()
    add=models.CharField(max_length=30)
    edu=models.CharField(max_length=30)

class prac1(models.Model):
    name=models.CharField(max_length=30)
    prac1_id = models.IntegerField()
    add = models.CharField(max_length=30)
    edu = models.CharField(max_length=30)
    phone=models.CharField(max_length=30)


