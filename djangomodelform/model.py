from __future__ import unicode_literals
from django.db import models


class studenteMobilis(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=50)
    gender = models.CharField()
    age = models.IntegerField()
    Dob = models.DateField()
    upload = models.ImageField()

    class Meta:
        db_table = "student"
