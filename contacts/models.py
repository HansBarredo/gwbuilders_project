from django.db import models
from datetime import datetime

class Contact(models.Model):
    name = models.CharField(max_length=100)  
    email = models.EmailField()
    phone = models.CharField(max_length=15, null=True, blank=True)
    subject = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()
    contact_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name