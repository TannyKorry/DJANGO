from django.contrib import admin
from django.urls import path
from .views import CreateSensorAPIViews, SensorView, SensorDetailAPIViews, CreateMeasurementAPIViews, SensorUpdateAPIViews

urlpatterns = [
    path('sensor/', CreateSensorAPIViews.as_view()), # создать датчик + получить список датчиков
    path('data/', CreateMeasurementAPIViews.as_view()), # создать измерение + получить список всех замеров
    path('sensor/update/<pk>', SensorUpdateAPIViews.as_view()), # обновить инфу по датчику
    path('sensor/<pk>', SensorDetailAPIViews.as_view()), # получить данные по конкретному датчику

]
