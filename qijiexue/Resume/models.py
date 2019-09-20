from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=500)
    createdate = models.DateField("Date", default=timezone.now)

    def __str__(self):
        return self.email
