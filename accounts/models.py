from django.db import models

# Create your models here.


class Registration(models.Model):
    email = models.CharField(max_length=55, blank=True, default="")
    phone = models.CharField(max_length=10, blank=True, default="")
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=10)

    def __str__(self):
        return self.name
