
from django.db import models
from django.db.models.functions import datetime


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=30, null=False, verbose_name='Датчик')
    description = models.CharField(max_length=120, verbose_name='Описание')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.id}' #f'{self.name} - {self.discription}'


class Measurement(models.Model):
    measurements = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    data = models.DecimalField(max_digits=10, decimal_places=1, verbose_name='Температура')
    time = models.DateTimeField(auto_now_add=True, null=False, verbose_name='Время измерения')

    class Meta:
        ordering = ['-time']

    def __str__(self):
        metering = f'{self.data}C'
        date_time = str(self.time)[:19]
        return '%s: %s, %s: %s' % ('temperature', metering, 'created_ad', date_time)


