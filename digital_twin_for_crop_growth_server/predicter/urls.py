from django.urls import path

from . import views

app_name = "predicter"

urlpatterns = [
    path("predict/", views.predict, name="predict")
]