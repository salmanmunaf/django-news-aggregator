from django.db import models

# Create your models here.

class News(models.Model):
    headline = models.CharField(max_length=255, null=False)
    link = models.CharField(max_length=255, null=False)
    source = models.CharField(max_length=50, null=False)
    request_date = models.DateField()