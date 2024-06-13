from django.db import models

# Create your models here.

class ContactUs(models.Model):
    Full_Name = models.CharField(max_length=150)
    Email = models.EmailField(max_length=254)
    Phone_number = models.IntegerField()
    Message = models.TextField()
    saveimg = models.ImageField(upload_to="imges", null = True, blank = True)
    def __str__(self):
        return self.Email + " " + self.Full_Name