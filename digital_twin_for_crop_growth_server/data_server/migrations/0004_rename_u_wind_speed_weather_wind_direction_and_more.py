# Generated by Django 4.1.7 on 2024-04-17 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("data_server", "0003_rename_weatehr_type_name_weather_weather_type_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="weather", old_name="u_wind_speed", new_name="wind_direction",
        ),
        migrations.RenameField(
            model_name="weather", old_name="v_wind_speed", new_name="wind_speed",
        ),
    ]
