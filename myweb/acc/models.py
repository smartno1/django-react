from django.db import models

# Create your models here.
class Member(models.Model):
    id = models.IntegerField
    account = models.CharField(max_length=20)
    password = models.
    

