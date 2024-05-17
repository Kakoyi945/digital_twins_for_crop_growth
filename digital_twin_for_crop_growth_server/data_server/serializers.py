# serializers.py
from rest_framework import serializers
from .models import Crop, Weather

class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = '__all__'  # 或者列出你想要包含的字段

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = '__all__'