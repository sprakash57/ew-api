from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    role = models.IntegerField(default=0)
    phoe = models.CharField(max_length=13)
    zip_code = models.IntegerField()
    city = models.CharField(max_length=32)

    def __str__(self):
        return self.name
