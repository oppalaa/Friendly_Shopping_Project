from django.db import models

# Create your models here.
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=50)
    profile_picture=models.ImageField()
