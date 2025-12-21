from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class BlogUser(AbstractUser):
    age=model.PositiveIntegerField()
    maticnumber=models.CharField()
    
    def __str__(self):
        return self.matricnumber