from django.shortcuts import render
from data_server.models import Crop, Weather
from django.forms.models import model_to_dict
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from data_server.models import Crop
import pandas as pd
import numpy as np
import json
import os
from .utils import algorithm

# Create your views here.

def predict(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # locId = data['loc']
            # if not locId:
            #     return HttpResponse("Missing required parameters", status=400)
            date = data['time_val']
            if not date:
                return HttpResponse("Missing required parameters", status=400)
            cropType = data['crop_type']
            if not cropType:
                return HttpResponse("Missing required parameters", status=400)
            model = data['model']
            if not model:
                return HttpResponse("Missing required parameters", status=400)
            modelName = None
            modelType = 1 # 1为机器学习，2为深度学习
            if model == '多元线性回归':
                modelName = 'mlr'
                modelType = 1
            elif model == '支持向量回归':
                modelName = 'svr'
                modelType = 1
            elif model == '随机森林回归':
                modelName = 'rfr'
                modelType = 1
            elif model == 'LSTM':
                modelName = 'lstm'
                modelType = 2
            elif model == 'GRU':
                modelName = 'gru'
                modelType = 2
            data = data['data']
            if 'crops' not in data or 'weathers' not in data:
                return HttpResponse("Missing required parameters", status=400)
            res_df = None
            if modelType == 1:
                res_df = algorithm.ml_predict(data, modelName, cropType)
            elif modelType == 2:
                res_df = algorithm.dl_predict(data, modelName, cropType)
            # 将结果封装为一个Crop Model再变为json返回
            cropTypeName = settings.CROPTYPE_TO_CROPNAME[cropType]
            crop = Crop(time_val=date, crop_type=cropType, crop_type_name=cropTypeName, dvs=res_df.at[0, 'dvs'], wlv=res_df.at[0, 'wlv'], 
                        wst=res_df.at[0, 'wst'], wso=res_df.at[0, 'wso'], tagp=res_df.at[0, 'tagp'], lai=res_df.at[0, 'lai'])
            cropDict = model_to_dict(crop)
            print('predict result is')
            print(cropDict)
            return JsonResponse(cropDict)
        except Exception as e:
            return HttpResponse("An error occured" + str(e), status=500) 