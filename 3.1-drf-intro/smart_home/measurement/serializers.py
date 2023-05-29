from abc import ABCMeta

from rest_framework import serializers

from .models import *
# TODO: опишите необходимые сериализаторы


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class SensorUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['measurements', 'data', 'time']


# class SensorDetailSerializer(serializers.ModelSerializer):
#     data = MeasurementSerializer(read_only=True, many=True)
#
#     class Meta:
#         model = Sensor
#         fields = ['id', 'name', 'description', 'data']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = serializers.StringRelatedField(many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


