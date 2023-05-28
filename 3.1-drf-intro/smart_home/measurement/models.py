from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=30, null=False, verbose_name='Датчик')
    description = models.CharField(max_length=120, verbose_name='Описание')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.id}' #f'{self.name} - {self.discription}'

    def __repr__(self):
        return f'{self.name} - {self.discription}'

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='sensor')
    data = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Температура')
    time = models.DateTimeField(auto_now_add=True, null=False, verbose_name='Время измерения')

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return self.time

    def __repr__(self):
        return f'{self.data} {self.time}'