import json
import datetime

with open("weather.json", "r") as weather:
    weather_data = json.loads(weather.read())

print(weather_data["name"])
print(weather_data["sys"]["country"])
print(weather_data["main"]["temp"])
print(weather_data["weather"][0]["description"])
print(datetime.datetime.fromtimestamp(weather_data["sys"]["sunrise"]))
print(datetime.datetime.fromtimestamp(weather_data["sys"]["sunset"]))

