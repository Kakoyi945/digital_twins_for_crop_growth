from django.test import TestCase, Client

# Create your tests here.
import json

class MyTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
    
    def test_predict(self):
        data = {
            'loc': 1,
            'model':'LSTM',
            'time_val':'2023-09-11',
            'crop_type':1,
            'data': {
                'weathers': [
                    {
                        'time_val':'2023-09-05',
                        'precipitation':1.3572638970504867e-05,
                        'surface_solar_radiation':20569989.455376968,
                        'temperature':300.1315029492909,
                        'wind_speed':82.61051516811753,
                        'wind_direction':178.240476613447,
                    }, 
                    {
                        'time_val':'2023-09-06',
                        'precipitation':3.639934996628458e-05,
                        'surface_solar_radiation':21400120.0209818,
                        'temperature':300.50793492919854,
                        'wind_speed':69.74491110251735,
                        'wind_direction':178.3636256047939,
                    },    
                    {
                        'time_val':'2023-09-07',
                        'precipitation':4.380260758655649e-05,
                        'surface_solar_radiation':20042720.674794808,
                        'temperature':301.5537513634069,
                        'wind_speed':37.0225778813212,
                        'wind_direction':180.1831251634996,
                    },   
                    {
                        'time_val':'2023-09-08',
                        'precipitation':0.0007100957934107,
                        'surface_solar_radiation':18720823.21657719,
                        'temperature':300.8660216145476,
                        'wind_speed':45.3242077047503,
                        'wind_direction':180.1567184209824,
                    },
                    {
                        'time_val':'2023-09-09',
                        'precipitation':0.0262815645519534,
                        'surface_solar_radiation':17138578.579917513,
                        'temperature':298.8594839840104,
                        'wind_speed':41.83461111056155,
                        'wind_direction':178.02641009487468,
                    },
                    {
                        'time_val':'2023-09-10',
                        'precipitation':0.0036664633364379,
                        'surface_solar_radiation':15375756.439018557,
                        'temperature':298.7119810835405,
                        'wind_speed':12.479365228470478,
                        'wind_direction':177.99628463188833,
                    },
                    {
                        'time_val':'2023-09-11',
                        'precipitation':0.0036664633364379,
                        'surface_solar_radiation':15375756.439018557,
                        'temperature':298.7119810835405,
                        'wind_speed':12.479365228470478,
                        'wind_direction':177.99628463188833,
                    },
                ],
                'crops': [
                    {
                        'time_val':'2023-09-05',
                        'dvs':1.89,
                        'wlv':1661,
                        'wst':1748,
                        'wso':7310,
                        'tagp':12077,
                        'lai':6.17
                    },
                    {
                        'time_val':'2023-09-06',
                        'dvs':1.92,
                        'wlv':1573,
                        'wst':1716,
                        'wso':7483,
                        'tagp':12252,
                        'lai':5.87
                    },
                    {
                        'time_val':'2023-09-07',
                        'dvs':1.94,
                        'wlv':1444,
                        'wst':1683,
                        'wso':7659,
                        'tagp':12431,
                        'lai':5.43
                    },
                    {
                        'time_val':'2023-09-08',
                        'dvs':1.96,
                        'wlv':1317,
                        'wst':1651,
                        'wso':7827,
                        'tagp':12600,
                        'lai':4.99
                    },
                    {
                        'time_val':'2023-09-09',
                        'dvs':1.99,
                        'wlv':1190,
                        'wst':1619,
                        'wso':7985,
                        'tagp':12758,
                        'lai':4.54
                    },
                    {
                        'time_val':'2023-09-10',
                        'dvs':2.02,
                        'wlv':1119,
                        'wst':1586,
                        'wso':8131,
                        'tagp':12905,
                        'lai':4.29
                    },
                    {
                        'time_val':'2023-09-11',
                        'dvs':0.0,
                        'wlv':0,
                        'wst':0,
                        'wso':0,
                        'tagp':0,
                        'lai':0.0
                    }
                ]
            }
        }
        data_json = json.dumps(data)
        headers = {'Content-Type':'application/json'}
        response = self.client.post('/predicter/predict/', content_type='application/json', data=data_json, **headers)
        
        print(response.status_code)
        print(response.content.decode())