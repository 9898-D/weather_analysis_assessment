from django.db import models

class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.FloatField()
    condition = models.CharField(max_length=100)
    wind_speed = models.FloatField()
    pressure = models.FloatField()
    visibility = models.FloatField()
    uv_index = models.FloatField()
    feels_like = models.FloatField()
    recorded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.city} - {self.temperature}°C - {self.condition}'
