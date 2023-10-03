from django.db import models

# Create your models here.

class ContactUs(models.Model):
    Name = models.CharField(max_length=100)
    Number = models.CharField(max_length=10)
    Emial = models.CharField(max_length=100)
    Message = models.TextField()