from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class SparkUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # This field is just to check that this user has filled out their profiles.
    profile_filled = models.BooleanField(default=False)
    # Relevant Fields..
    name = models.CharField(max_length=100, default="No Name")
    image = models.ImageField(upload_to='images/',
                             default='data/jisungpark1.jpg')
    email = models.CharField(max_length=100, default = "No Emails")
    age = models.IntegerField()
    gender = models.CharField(max_length=30)
    interest = models.CharField(max_length=150, default = "No interest")

