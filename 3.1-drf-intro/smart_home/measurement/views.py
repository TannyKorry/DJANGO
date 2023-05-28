# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from .models import *
from .serializers import *
from rest_framework.response import Response


class CreateSensorAPIViews(ListCreateAPIView): # Создать датчик. Указываются название и описание датчика.
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetailAPIViews(RetrieveAPIView): # Получить список датчиков. Выдаётся список с краткой информацией по датчикам: ID, название и описание.
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class SensorUpdateAPIViews(RetrieveUpdateAPIView): # Изменить датчик. Указываются название и описание.
    queryset = Sensor.objects.all()
    serializer_class = SensorUpdateSerializer


class CreateMeasurementAPIViews(ListCreateAPIView): # Добавить измерение. Указываются ID датчика и температура.
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SensorView(RetrieveAPIView): # Получить информацию по конкретному датчику. Выдаётся полная информация по датчику: ID, название, описание и список всех измерений с температурой и временем.
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


