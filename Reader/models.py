from django.db import models

# Create your models here.
class Person(models.Model):
  name = models.CharField(max_length = 50)
  email = models.EmailField()
  location = models.CharField(max_length = 50, blank = True)