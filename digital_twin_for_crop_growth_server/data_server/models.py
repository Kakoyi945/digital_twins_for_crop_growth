from django.db import models

# Create your models here.
class Location(models.Model):
    statnum = models.IntegerField(default=0)
    statCName = models.CharField(max_length=20)
    statEName = models.CharField(max_length=20)
    provCname = models.CharField(max_length=20)
    provEname = models.CharField(max_length=20)
    lon = models.FloatField(default=0)
    lat = models.FloatField(default=0)

    def __str__(self):
        return f'Location(\
                statnum: {self.statnum}, \
                statCName: {self.statCName}\
                statEName: {self.statEName}\
                provCname: {self.provCname}\
                lon: {self.lon}\
                lat: {self.lat})'

class Weather(models.Model):
    time_val = models.CharField(max_length=20)
    weather_type = models.IntegerField(default=0)
    weather_type_name = models.CharField(max_length=20)
    precipitation = models.FloatField(default=0)
    surface_solar_radiation = models.FloatField(default=0)
    wind_speed = models.FloatField(default=0)
    wind_direction = models.FloatField(default=0)
    temperature = models.FloatField(default=0)
    loc = models.ForeignKey(Location, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'Weather(\
            time_val: {self.time_val}\
            weather_type: {self.weather_type}\
            weather_type_name: {self.weather_type_name}\
            precipitation: {self.precipitation}\
            surface_solar_radiation: {self.surface_solar_radiation}\
            wind_speed: {self.wind_speed}\
            wind_direction: {self.wind_direction}\
            temperature: {self.temperature}\
            loc: {self.loc})'

class Crop(models.Model):
    time_val = models.CharField(max_length=20)
    crop_type = models.IntegerField(default=0)
    crop_type_name = models.CharField(max_length=20)
    dvs = models.FloatField(default=0)
    wlv = models.IntegerField(default=0)
    wst = models.IntegerField(default=0)
    wso = models.IntegerField(default=0)
    tagp = models.IntegerField(default=0)
    lai = models.FloatField(default=0)
    loc = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Crop(\
                time_val: {self.time_val}\
                crop_type: {self.crop_type}\
                crop_type_name: {self.crop_type_name}\
                dvs: {self.dvs}\
                wlv: {self.wlv}\
                wst: {self.wst}\
                wso: {self.wso}\
                tagp: {self.tagp}\
                lai: {self.lai}\
                loc: {self.loc})'