from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
# 对于数组
from django.core.serializers import serialize
# 对于单个models
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from .models import Location, Weather, Crop
from .serializers import CropSerializer, WeatherSerializer
# from django.core.cache import cache
import json

def index(request):
    return HttpResponse("Hello, world. You're at the data_server index.")

# def test(request):
#     loc = get_object_or_404(Location, statCName="齐河", provCname="山东")
#     return render(request, "data_server/index.html", {"location": loc})

def all_locations(request):
    try:
        locs = Location.objects.all()
        locsJson = serialize('json', locs)
        return HttpResponse(locsJson, content_type='application/json') 
    except Exception as e:
        return HttpResponse("An error occurred" + str(e), status=500)

def location(request):
    queryString = request.GET
    try:
        statName = queryString['statName']
        provName = queryString['provName']
        if not statName or not provName:
            return HttpResponse("Missing required parameters", status=400)
        # print(statName + provName)
        loc = get_object_or_404(Location, statCName=statName, provCname=provName)
        # return render(request, {"location": loc})
        locDict = model_to_dict(loc)
        print(locDict)
        # # 将数据保存在cache中，方便predict使用
        # cache.set('location', json.dumps(locDict))
        return JsonResponse(locDict)
    except Exception as e:
        return HttpResponse("An error occurred" + str(e), status=500)

def current_crop(request):
    queryString = request.GET
    try:
        cropType = queryString['crop_type']
        curDate = queryString['cur_date']
        if not curDate:
            return HttpResponse("Missing required parameters", status=400)
        curCrop = get_object_or_404(Crop, time_val=curDate, crop_type=cropType)
        curCropDict = model_to_dict(curCrop)
        # # # 将crop存入cache中，方便predict使用
        # cachedCrops = json.loads(json.dumps(cache.get('crops')))
        # cachedCrops.append(curCropDict)
        # # print(cachedCrops)
        # cache.set('crops', json.dumps(cachedCrops))
        return JsonResponse(curCropDict)
    except Exception as e:
        return HttpResponse("An error occured" + str(e), status=500)

def current_weather(request):
    queryString = request.GET
    try:
        curDate = queryString['cur_date']
        if not curDate:
            return HttpResponse("Missing required parameters", status=400)
        # curCrop = get_object_or_404(Crop, time_val=curTime, crop_type=cropType)
        curWeather = get_object_or_404(Weather, time_val=curDate)
        print(curWeather)
        curWeatherDict = model_to_dict(curWeather)
        print(curWeatherDict)
        # # 将weather保存到cache中，方便predict使用
        # cachedWeather = json.loads(cache.get('weathers'))
        # cachedWeather.append(curWeatherDict)
        # print(cachedWeather)
        # cache.set('weathers', json.dumps(cachedWeather))
        return JsonResponse(curWeatherDict)
    except Exception as e:
        return HttpResponse("An error occured" + str(e), status=500)

def to_current_weathers(request):
    queryString = request.GET
    try:
        start_date = queryString['start_date']
        cur_date = queryString['cur_date']
        if not start_date or not cur_date:
            return HttpResponse("Missing required parameters", status=400)
        sortedWeathers = Weather.objects.order_by('time_val').filter(time_val__range=(start_date, cur_date))
        serializer = WeatherSerializer(sortedWeathers, many=True)
        data = serializer.data
        print(data)
        # # 保存到cache中，方便predict使用
        # cache.set('weathers', json.dumps(data))
        return JsonResponse(data, safe=False)
    except Exception as e:
        return HttpResponse("An error occured" + str(e), status=500)

def to_current_crops(request):
    queryString = request.GET
    try:
        crop_type = queryString['crop_type']
        start_date = queryString['start_date']
        cur_date = queryString['cur_date']
        if not crop_type or not start_date or not cur_date:
            return HttpResponse("Missing required parameters", status=400)
        # 选择crops中crop_type为crop_type的所有行，再将行按照time_val从小到大排序，最后选择范围在startTime到curTime之间的数据，包括startTime和curTime
        sortedCrops = Crop.objects.filter(crop_type=crop_type).order_by('time_val').filter(time_val__range=(start_date, cur_date))
        serializer = CropSerializer(sortedCrops, many=True)
        data = serializer.data
        # print(data)
        # # 保存到cache中
        # cache.set('crops', data)
        return JsonResponse(data, safe=False)
    except Exception as e:
        return HttpResponse("An error occured" + str(e), status=500)


# def test(request):
#     params = request.GET
#     params_str = '&'.join([f'{key}={value}' for key, value in params.items()])

#     return HttpResponse(params_str)
    