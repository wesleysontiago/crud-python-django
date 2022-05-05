from unicodedata import name
from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    phone = models.CharField(max_length=15)
    birth_day = models.CharField(max_length=10)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')
