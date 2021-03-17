from django.db import models

# Create your models here.
class Compute(models.Model):
    number = models.IntegerField(null=True)
    serie_fibonacci = models.CharField(max_length=500, null=True)


def fibonacci(n):
       if n <= 1:
           return n
       else:
           return fibonacci(n-1) + fibonacci(n-2)    



