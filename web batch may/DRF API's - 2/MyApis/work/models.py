from django.db import models

# Create your models here.

class contactus(models.Model):
    first_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    phone_number = models.IntegerField()
    message = models.TextField()