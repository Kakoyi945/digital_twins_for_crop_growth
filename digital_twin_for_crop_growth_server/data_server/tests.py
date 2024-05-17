from django.test import TestCase, Client

# Create your tests here.
from .models import Location, Crop, Weather
import json


class MyTestCase(TestCase):
    def setUp(self):
        loc = Location.objects.create(statnum=0, statCName='齐河', statEName='QiHe', \
                                provCname='山东', provEname='Shandong', lon = 0.0, lat=0.0)
        Crop.objects.create(time_val='20231231', crop_type=1, crop_type_name='小麦',\
                            dvs=0.15, wlv=149, wst=18, wso=0, tagp=167, lai=0.29, loc=loc)
        Weather.objects.create(time_val='20231231', weather_type=0, weather_type_name='Overcast',\
                               precipitation=1.0, wind_speed=1.0, wind_direction=1.0, temperature=30.0, loc=loc)
        self.client = Client()

    def test_locations(self):
        response = self.client.get('/data_server/all_locations/')
        json_data = json.loads(response.content)
        print('locations_test')
        print(json_data)
        

    def test_location(self):
        data = {'statName': '齐河', 'provName': '山东'}
        response = self.client.get('/data_server/location/', data)
        json_data = json.loads(response.content)
        print('location test')
        print(json_data)
        # print(response.content)
