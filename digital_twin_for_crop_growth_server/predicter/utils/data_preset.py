import pandas as pd
import numpy as np
import torch
from . import config
from datetime import datetime, timedelta 

def change_data_to_ml_data(data):
    input = []
    for i in range(len(data['weathers'])):
        weather = data['weathers'][i]
        d_str = weather['time_val']
        d = datetime.strptime(d_str, '%Y-%m-%d')
        year = int(d.strftime("%Y"))
        month = int(d.strftime("%m"))
        day = int(d.strftime("%d"))
        new_list = [year, month, day]
        precipitation = float(weather['precipitation'])
        new_list.append(precipitation)
        surface_solar_radiation = float(weather['surface_solar_radiation'])
        new_list.append(surface_solar_radiation)
        temperature = float(weather['temperature'])
        new_list.append(temperature)
        wind_speed = float(weather['wind_speed'])
        new_list.append(wind_speed)
        wind_direction = float(weather['wind_direction'])
        new_list.append(wind_direction)
        crop = data['crops'][i]
        dvs = float(crop['dvs'])
        new_list.append(dvs)
        wlv = int(crop['wlv'])
        new_list.append(wlv)
        wst = int(crop['wst'])
        new_list.append(wst)
        wso = int(crop['wso'])
        new_list.append(wso)
        tagp = int(crop['tagp'])
        new_list.append(tagp)
        lai = float(crop['lai'])
        new_list.append(lai)
        input.append(new_list)
    input = pd.DataFrame(input, columns=config.ml_columns)
    print(input)
    return input

def change_data_to_dl_data(data):
    input = []
    input_ = []
    for i in range(len(data['weathers'])):
        weather = data['weathers'][i]
        d_str = weather['time_val']
        d = datetime.strptime(d_str, '%Y-%m-%d')
        # year = int(d.strftime("%Y"))
        month = int(d.strftime("%m"))
        day = int(d.strftime("%d"))
        new_list = [month, day]
        new_list.append(float(weather['precipitation']))
        new_list.append(float(weather['surface_solar_radiation']))
        new_list.append(float(weather['temperature']))
        new_list.append(float(weather['wind_speed']))
        new_list.append(float(weather['wind_direction']))
        input.append(new_list)
    for i in range(len(data['crops'])-1):
        crop = data['crops'][i]
        new_list = []
        new_list.append(float(crop['dvs']))
        new_list.append(int(crop['wlv']))
        new_list.append(int(crop['wst']))
        new_list.append(int(crop['wso']))
        new_list.append(int(crop['tagp']))
        new_list.append(float(crop['lai']))
        input_.append(new_list)     
    return input, input_


        
        