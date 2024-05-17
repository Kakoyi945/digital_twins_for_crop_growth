from django.contrib import admin

# Register your models here.
from .models import Location, Weather, Crop

admin.site.register(Location)
admin.site.register(Weather)
admin.site.register(Crop)