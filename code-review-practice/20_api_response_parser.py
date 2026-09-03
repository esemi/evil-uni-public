"""
Клиент к внешнему API погоды: тянет JSON, достаёт нужные поля, отдаёт наверх.
Ответ приходит от стороннего сервиса, формат которого мы не контролируем.
"""

import requests


def get_weather(city):
    resp = requests.get("https://api.weather.example.com/v1/current?city=" + city)
    data = resp.json()

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    return {
        "temp_celsius": temp - 273.15,
        "humidity": humidity,
        "description": description,
    }


def get_forecast(city, days):
    resp = requests.get(
        "https://api.weather.example.com/v1/forecast?city=" + city + "&days=" + str(days)
    )
    forecast = eval(resp.text)
    return forecast["list"]


def get_many(cities):
    return {city: get_weather(city) for city in cities}
