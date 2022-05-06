from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    phone = models.CharField(max_length=15)
    birthDay = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.owner)+''
