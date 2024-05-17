from django.urls import path

from . import views

app_name = "data_server"

urlpatterns = [
    # ex:/data_server/
    # path("", views.test, name="index"),
    # ex:/data_server/location?statName=xxx&provName=xxx
    path("all_locations/", views.all_locations, name="allLocations"),
    path("location/", views.location, name="getLocation"),
    # ex:/data_server/current?date=20241203
    path("current_crop/", views.current_crop, name="getCurrentCrop"),
    path("current_weather/", views.current_weather, name="getCurrentWeather"),
    path("current_crops/", views.to_current_crops, name="getCurrentCrops"),
    path("current_weathers/", views.to_current_weathers, name="getCurrentWeathers"),

    # path("test/", views.test, name="test")
    # path("send/", views.send, name="send"),
]