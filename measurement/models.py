from django.db import models
from PIL import Image

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=300, blank=True)


class Measurement(models.Model):
    sensor = models.ForeignKey(
        Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='measurements/', null=True, blank=True)
