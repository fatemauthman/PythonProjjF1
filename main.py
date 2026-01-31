import streamlit as st
import requests
import pandas as pd
from datetime import datetime, timezone, timedelta

# =========================
# App Configuration
# =========================
st.set_page_config(page_title="Weather App", page_icon="")
st.title(" Weather Checker App")

# --- Name section ---
st.subheader("👋 Welcome")
name = st.text_input("Enter your name", key="name_input")

if name:
    st.success(f"Hello {name}! 😊 Welcome to the Weather App")
api_key = "631e6df9a39414ae72d5ad878b96c13e"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# =========================
# Functions
# =========================
def get_weather(city, api_key, units="metric"):
    params = {
        "q": city,
        "appid": API_KEY,
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
        "timezone": data["timezone"],
        "lat": data["coord"]["lat"],
        "lon": data["coord"]["lon"]
    }


def get_location_time(timezone_offset):
    utc_time = datetime.now(timezone.utc)
    location_time = utc_time + timedelta(seconds=timezone_offset)
    return location_time.strftime("%A, %d %B %Y, %H:%M")


# =========================
# UI
# =========================
city = st.text_input("Enter city name", key="city_input")

if st.button("Get Weather", key="get_weather_btn") and city:
    try:
        weather_data = get_weather(city)

        st.subheader(f" Weather in {weather_data['city']}")
        st.write(f" **Temperature:** {weather_data['temperature']} °C")
        st.write(f" **Humidity:** {weather_data['humidity']}%")
        st.write(f" **Condition:** {weather_data['condition']}")

        # Date & Time
        location_time = get_location_time(weather_data["timezone"])
        st.subheader(" Local Date & Time")
        st.write(location_time)

        # Map
        st.subheader(" Location on Map")
        map_df = pd.DataFrame({
            "lat": [weather_data["lat"]],
            "lon": [weather_data["lon"]]
        })
        st.map(map_df)

    except requests.exceptions.HTTPError:
        st.error(" City not found. Please try again.")

    except Exception as e:
        st.error(" Something went wrong.")
