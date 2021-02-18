from django.db import models

# Create your models here.


class Registration(models.Model):
    email = models.CharField(max_length=50, blank=True, default="")
    phone = models.CharField(max_length=10, blank=True, default="")
    password = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=True)

    def __str__(self):
        return self.name
