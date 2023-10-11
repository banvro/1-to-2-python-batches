from django.db import models

# Create your models here.


class ContactUs(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Number = models.IntegerField()
    Email = models.CharField(max_length=50)
    Message = models.TextField()