from django.db import models

# Create your models here.
class Detection(models.Model):
    device_id=models.CharField(max_length=100, blank=True)
    lng=models.CharField(max_length=20, blank=True)
    lat=models.CharField(max_length=20, blank=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)



