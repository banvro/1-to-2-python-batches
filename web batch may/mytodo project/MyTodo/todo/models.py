from django.db import models

# Create your models here.


class savetodo(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)