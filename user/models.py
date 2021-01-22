from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    role = models.IntegerField()

    def __str__(self):
        return self.name
