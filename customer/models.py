from django.db import models

# Create your models here.

class Details(models.Model):
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=14)

    def __str__(self):
        return self.name