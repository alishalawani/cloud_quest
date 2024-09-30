from django.db import models

# Create your models here.

class Machine(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # Size can represent disk size_gb or another dimension
    size_gb = models.PositiveIntegerField(default=0)  # Size in gigabytes
    operating_system = models.CharField(
        max_length=50, default="Mac")  # Default OS
    status = models.CharField(max_length=20, choices=[
        ('running', 'Running'),
        ('stopped', 'Stopped'),
        ('paused', 'Paused'),
    ], default='stopped')

    def __str__(self):
        return f"{self.name} - Size: {self.size_gb}, OS: {self.operating_system}, Status: {self.status}"
