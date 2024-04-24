from django.db import models

class Taxi(models.Model):
    plate_number = models.CharField(max_length=20, unique=True)
    model = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='taxi_images', null=True, blank=True)

    def __str__(self):
        return f"{self.plate_number} - {self.model}"
