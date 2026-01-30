import requests
from datetime import datetime, timezone, timedelta

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city, api_key, units="metric"):
    ...

def get_location_time(timezone_offset):
    utc_time = datetime.now(timezone.utc)
    location_time = utc_time + timedelta(seconds=timezone_offset)
    return location_time.strftime("%A, %d %B %Y, %H:%M")

from datetime import datetime, timezone, timedelta


            def get_location_time(timezone_offset):
                """
                timezone_offset: offset in seconds from UTC (from OpenWeatherMap)
                """