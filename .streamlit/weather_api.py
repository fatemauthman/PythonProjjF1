import requests
from datetime import datetime, timezone, timedelta

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city, api_key, units="metric"):
    params = {
        "q": city,
        "appid": api_key,
        "units": units
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()

    return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "condition": data["weather"][0]["description"],
        "timezone": data["timezone"]
    }

def get_location_time(timezone_offset):
    utc_time = datetime.now(timezone.utc)
    location_time = utc_time + timedelta(seconds=timezone_offset)
    return location_time.strftime("%A, %d %B %Y, %H:%M")
